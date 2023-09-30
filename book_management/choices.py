from django.db import models


class BookConditions(models.TextChoices):
    NEW = 'New'
    SECOND_HAND = 'Second Hand'
