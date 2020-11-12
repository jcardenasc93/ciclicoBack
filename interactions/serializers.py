from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Club, Event, Route, AppUser, Benefit

class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AppUserSerializer(ModelSerializer):
    user_club = serializers.PrimaryKeyRelatedField(
        queryset=Club.objects.all(),
        many=True
    )
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'edition', 'user_club']


class RoutesSerializer(ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=AppUser.objects.all(),
        read_only=False,
        slug_field='email'
    )
    class Meta:
        model = Route
        fields = ['id', 'name', 'country', 'city', 'start_latitude', 'start_longitude',
                  'end_latitude', 'end_longitude', 'distance_kms', 'user', 'created_at']

class BenefitSerializer(ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'