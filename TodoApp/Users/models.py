from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Owner(User):
    """Inherited Model definition for Owners"""
    orderList = models.TextField()