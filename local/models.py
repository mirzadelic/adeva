from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=100)
    authors = ArrayField(models.CharField(max_length=100))
    country = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    release_date = models.DateField()

    class Meta:
        ordering = ('-release_date',)
