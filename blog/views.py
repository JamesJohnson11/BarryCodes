from django.shortcuts import render
from .models import Post


def all_blog_posts(request):
    return render(request, 'blog/templates/all_posts.html')
