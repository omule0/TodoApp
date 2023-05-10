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
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    remind_minutes = models.IntegerField(default=0)
    is_skipped = models.BooleanField(default=False)

    def toggle_completed(self):
        self.completed = not self.completed
        self.save()
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-due_date']