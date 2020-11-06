from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.city}, {self.country}'

class Event(models.Model):
    name = models.CharField(max_length=255)
    location_latitude = models.CharField(max_length=100, blank=True, null=True)
    location_longitude = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='event_club')

    def __str__(self):
        return f'{self.name} - {self.club.name}'


class AppUser(models.Model):
    email = models.CharField(max_length=150, unique=True)
    edition = models.CharField(max_length=50)
    user_club = models.ManyToManyField(Club, through='ClubAppUser', null=True, blank=True)

    def __str__(self):
        return self.email

class ClubAppUser(models.Model):
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING)
    app_user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING, to_field='email')

    class Meta:
        unique_together = (('club', 'app_user'),)

class Route(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    start_latitude = models.CharField(max_length=100)
    start_longitude = models.CharField(max_length=100)
    end_latitude = models.CharField(max_length=100)
    end_longitude = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name='route_user')
    created_at = models.DateField(auto_now_add=True)

