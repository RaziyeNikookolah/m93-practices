from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    national_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_addresses")

    def __str__(self):
        return f'{self.city}'


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')

    def __str__(self):
        return f'{self.body}'
