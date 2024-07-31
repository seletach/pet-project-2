from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'blog/index.html')


def profile(request):
    return render(request, 'blog/profile.html')


def post_form(request):
    form = PostForm(request.POST or None)
    # if form.is_valid():
    #     form.save() 

    context = {
        'title': request.user,
        'text': request.POST.get('text'),
        'form': form,
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post_form.html', context)