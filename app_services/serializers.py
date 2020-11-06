from rest_framework import serializers
from .models import RentPoint, MaintanceStore, TheftReport, AppUser

class MaintanceStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintanceStore
        fields = '__all__'

class RentPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentPoint
        fields = '__all__'

class TheftReportSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=AppUser.objects.all(),
        slug_field='email',
        read_only=False
    )
    class Meta:
        model = TheftReport
        fields = ['id', 'country', 'city', 'description', 'user', 'created_at']