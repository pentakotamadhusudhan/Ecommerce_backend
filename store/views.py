from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from generic_reponse import failed_response, success_response
from .models import Product, Order, Store
from .serializers import ProductSerializer, OrderSerializer, StoreSerializer
from accounts.permissions import IsManager, IsStaff
from .permissions import IsVendor, IsOwnerVendor


class StoreViewSet(GenericAPIView):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsVendor]

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save(vendor=request.user)

            return success_response(
                message="Store created successfully",
                data=serializer.data,
                status_code=status.HTTP_201_CREATED
            )

        except Exception as e:
            print("STORE CREATE ERROR:", e)
            return failed_response(
                message="Internal server error",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
