"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import views
from interactions.views import ClubViewSet, EventViewSet, RouteViewSet, AppUserViewSet, BenefitViewSet
from analytics.views import DistanceViewSet
from app_services.views import RentPointViewSet, MaintanceStoreViewSet, TheftReportViewSet

router = DefaultRouter()
router.register(r'users', AppUserViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'events', EventViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'distances', DistanceViewSet)
router.register(r'maintance-stores', MaintanceStoreViewSet)
router.register(r'rent-points', RentPointViewSet)
router.register(r'theft-reports', TheftReportViewSet)
router.register(r'benefits', BenefitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/', include(router.urls)),
]
