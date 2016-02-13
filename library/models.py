from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    author = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{name} - {author}".format(
            name=self.name, author=self.author.get_username())

    class Meta:
        app_label = 'library'


class Library(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'library'
