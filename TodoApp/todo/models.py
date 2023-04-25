from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from Users.models import Owner


class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
      