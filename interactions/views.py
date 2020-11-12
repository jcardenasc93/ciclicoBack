from rest_framework.viewsets import ModelViewSet
from .models import Club, Event, Route, AppUser, Benefit
from .serializers import ClubSerializer, EventSerializer, RoutesSerializer, AppUserSerializer, BenefitSerializer
# Create your views here.

class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AppUserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RoutesSerializer

class BenefitViewSet(ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer