from django.contrib.auth.models import AbstractUser
from django.db import models
from versatileimagefield.fields import VersatileImageField

from book_management.choices import BookConditions
from user.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    condition = models.CharField(choices=BookConditions.choices, max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_books')
    location = models.CharField(max_length=200)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='received_books')
    image_poster = VersatileImageField(upload_to='book_posters/', blank=True, null=True)
