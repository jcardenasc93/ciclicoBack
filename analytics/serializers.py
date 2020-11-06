from rest_framework import serializers
from .models import Distance, AppUser

class DistanceSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=AppUser.objects.all(),
        slug_field='email',
        read_only=False
    )
    class Meta:
        model = Distance
        fields = ['id', 'distance_kms', 'time_s', 'user', 'created_at']
        
