from rest_framework.viewsets import ModelViewSet
from .models import Distance
from .serializers import DistanceSerializer

# Create your views here.
class DistanceViewSet(ModelViewSet):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer
