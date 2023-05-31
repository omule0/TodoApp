from django.db import models

class Event(models.Model):
    # Define your Event model fields here
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    # Add any other fields as needed

    def __str__(self):
        return self.title
