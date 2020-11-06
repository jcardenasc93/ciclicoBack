from django.db import models
from interactions.models import AppUser

# Create your models here.
class Distance(models.Model):
    distance_kms = models.DecimalField(max_digits=5, decimal_places=2)
    time_s = models.IntegerField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
