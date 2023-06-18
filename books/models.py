from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    genre = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    count = models.IntegerField(null=True, default=0)