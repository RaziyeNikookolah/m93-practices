from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    national_code = models.CharField(max_length=10)


class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_addresses")


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")





