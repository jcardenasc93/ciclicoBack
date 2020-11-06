from django.contrib import admin
from .models import Club, Event, Route
# Register your models here.
models = [Club, Event, Route]

admin.site.register(models,)
