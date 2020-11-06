from django.db import models
from interactions.models import AppUser

# Create your models here.
class MaintanceStore(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    still_open = models.BooleanField(default=True)

class RentPoint(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

class TheftReport(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)

