from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    author = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'library'


class Library(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    books = models.ManyToManyField(Book)

    class Meta:
        app_label = 'library'
