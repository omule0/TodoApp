from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
      