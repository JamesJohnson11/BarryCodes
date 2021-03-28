from django.shortcuts import render
from .models import Post


def all_blog_posts(request):
    return render(request, 'blog/all_posts.html')
