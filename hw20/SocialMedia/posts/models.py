from django.db import models
from accounts.models import User, Address


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')

    def __str__(self):
        return f'{self.body}'

    class Meta:
        verbose_name_plural = 'Comments'
