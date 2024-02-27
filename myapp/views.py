from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html', {'posts': post})


def portfolio_details(request):
    return render(request, 'portfolio_details.html')


def blog_single(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_single.html', {'post': post})
