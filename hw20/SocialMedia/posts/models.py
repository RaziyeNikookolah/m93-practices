from django.db import models
from accounts.models import User


class Post(models.Model):  # TODO it can have a date
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    createdAt = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    createdAt = models.DateField(auto_created=True)
    isActive=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author} says: {self.body} '

    class Meta:
        verbose_name_plural = 'Comments'
