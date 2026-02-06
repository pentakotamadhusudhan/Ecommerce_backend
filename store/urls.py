from rest_framework.routers import DefaultRouter
from .views import  StoreViewSet
from .products_view import *
from django.urls import path


urlpatterns = [
    path('create/', StoreViewSet.as_view(), name='stores'),
    path('addproducts/', ProductPostView.as_view(), name='products_post'),
    path('catagory/', CatagoryPostView.as_view(), name='catagory_post'),
]
