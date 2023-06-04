from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255,default='task')
    due_date = models.DateField(null=True, blank=True,default=timezone.now)
    due_time = models.TimeField(null=True, blank=True,default=timezone.datetime.strptime("12:00", "%H:%M").time())
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True,default='my todo task')
    completed = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)
    remind_minutes = models.IntegerField(default=5)
    is_skipped = models.BooleanField(default=False)

    def toggle_completed(self):
        self.completed = not self.completed
        self.save()
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-due_date']

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    due_time = models.TimeField(null=True, blank=True,default=timezone.now)
    week_of = models.DateField() 
    
    def __str__(self):
        return self.item
    
    class Meta:
        ordering = ['-week_of']