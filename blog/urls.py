from django.urls import path

urlpatterns = [
    path('', views.all_blog_posts, name='all_blog_posts'),
]