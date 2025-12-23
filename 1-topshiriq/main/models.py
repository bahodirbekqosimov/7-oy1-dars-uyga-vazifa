from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=55)
    year = models.CharField(max_length=15)
    price = models.IntegerField()
    