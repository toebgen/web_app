import datetime

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.name
