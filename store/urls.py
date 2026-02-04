from rest_framework.routers import DefaultRouter
from .views import  StoreViewSet
from django.urls import path


urlpatterns = [
    path('create/', StoreViewSet.as_view(), name='stores'),
]
