from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_details(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_details.html', {'post': post})


def all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/all_posts.html', {"posts": posts})
