from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import *
from .serializers import CatagorySerializer, ProductSerializer
from generic_reponse import *

class ProductPostView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    def post(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            serializer = ProductSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )


    def get(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            query = self.queryset.objects.all()
            serializer = self.serializer_class(query,many=True)
            
            if serializer:
                # serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )



class CatagoryPostView(GenericAPIView):
    serializer_class = CatagorySerializer
    queryset = ProductCategory
    def post(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            serializer = CatagorySerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )


    def get(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            query = self.queryset.objects.all()
            serializer = self.serializer_class(query,many=True)
            
            if serializer:
                # serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )

