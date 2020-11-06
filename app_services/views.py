from rest_framework.viewsets import ModelViewSet
from .models import MaintanceStore, RentPoint, TheftReport
from .serializers import MaintanceStoreSerializer, RentPointSerializer, TheftReportSerializer

# Create your views here.
class MaintanceStoreViewSet(ModelViewSet):
    queryset = MaintanceStore.objects.all()
    serializer_class = MaintanceStoreSerializer

class RentPointViewSet(ModelViewSet):
    queryset = RentPoint.objects.all()
    serializer_class = RentPointSerializer

class TheftReportViewSet(ModelViewSet):
    queryset = TheftReport.objects.all()
    serializer_class = TheftReportSerializer