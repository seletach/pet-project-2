from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comments
from .forms import PostForm, CommentForm
from users.models import MyUser


def form_save(method, post_id=None):
    pass


def index(request):
    return render(request, 'blog/index.html')


def post_form(request):
    
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
        'posts': Post.objects.all().order_by('id')
    }
    return render(request, 'blog/post_form.html', context)


def post_card(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = id
            comment.save()
    else:
        form = CommentForm()

    context = {
        'post': post,
        'author': MyUser.objects.get(id=post.author_id),
        'comment_form': CommentForm,
        'comments': Comments.objects.filter(post_id=id)
    }
    return render(request, 'blog/post_card.html', context)
