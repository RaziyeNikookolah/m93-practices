from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Comment
from accounts.models import User


def post_details(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        comments=Comment.objects.filter(post=post)
        comments_count=comments.count()
        return render(request, 'posts/post_details.html', {'post': post,"comments":comments, "comments_count":comments_count})


def all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/all_posts.html', {"posts": posts})


def user_posts(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(author=user)
        return render(request, 'posts/user_posts.html', {"posts": posts, "user": user})
