from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True,default=timezone.now)
    due_time = models.TimeField(null=True, blank=True,default=timezone.datetime.strptime("09:00", "%H:%M").time())
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

class List(models.Model):
    DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    due_time = models.TimeField(null=True, blank=True)
    week_of = models.CharField(max_length=10, choices=DAY_CHOICES)
    due_week = models.DateField()  
    

    def __str__(self):
        return self.item
    
    class Meta:
        ordering = ['-week_of']