from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    national_code = models.CharField(max_length=10)
    address = models.ForeignKey(
        "Address",
        on_delete=models.CASCADE,
    )


class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
