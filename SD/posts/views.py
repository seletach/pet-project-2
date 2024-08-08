from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comments
from .forms import PostForm, CommentForm
from users.models import MyUser


def index(request):
    return render(request, 'blog/index.html')


def post_create(request):
    """
    Форма написания поста
    """
    
    message = 'Написание поста'
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()

    context = {
        'form': PostForm,
        'count': Post.objects.count(),
        'posts': Post.objects.all().order_by('id'),
        'message': message
    }
    return render(request, 'blog/post_create.html', context)


def post_update(request, post_id):
    """
    Форма редактирования поста
    """
    
    message = 'Редактирование поста'
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/post/'+ f'{post_id}/')
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'blog/post_create.html', context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user == post.author:
        post.delete()
        return redirect('blog:post_create')
    else: context = { 'message_error': 'Удалять может только автор поста!' }

    return render(request, 'blog/post_card.html', context)


def comment_edit(request, post_id, comment_id):
    """
    Редактирование комментария
    """

    instance = get_object_or_404(Comments, id=comment_id, post_id=post_id)
    form = CommentForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/post/'+ f'{post_id}/')
    context = {
        'comment_form': form
    }
    return render(request, 'blog/post_card.html', context)


def post_card(request, post_id):
    """
    Карточка поста с информацией и комментариями
    """

    post = Post.objects.get(id=post_id)
    comments = Comments.objects.filter(post_id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm,
    }
    return render(request, 'blog/post_card.html', context)
