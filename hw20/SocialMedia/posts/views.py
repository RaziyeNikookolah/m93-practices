from datetime import datetime
from django.shortcuts import render
from .models import Post, Comment
from .forms import CreateCommentForm, CreatePostForm
from accounts.models import User


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    comments_count = comments.count()
    form = CreateCommentForm()
    if request.method == 'POST':
        user = User.objects.filter(last_name=request.POST['author'])
        if user[0]:
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                initial_data = {'createdAt': datetime.now(),
                                'post': post,
                                'author': user[0],
                                'isActive': True,
                                'body': cd['body']}
                Comment.objects.create(**initial_data)

    return render(request, 'posts/post_details.html',
                  {"form": form, 'post': post, "comments": comments, "comments_count": comments_count})


def all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/all_posts.html', {"posts": posts})


def user_posts(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(author=user)
        return render(request, 'posts/user_posts.html', {"posts": posts, "user": user})


def add_post(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'GET':
        form = CreatePostForm()
        return render(request, 'posts/add_post.html',
                      {"form": form, "user": user})
    elif request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            initial_data = {'createdAt': datetime.now(),
                            "title": cd['title'],
                            'author': user,
                            'isActive': True,
                            'body': cd['body'],
                            "image": ""}
            Post.objects.create(**initial_data)
            posts = Post.objects.all()
            return render(request, 'posts/all_posts.html',
                          {"form": form, 'posts': posts})
