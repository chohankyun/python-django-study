from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False)

