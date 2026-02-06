import http
from django.db.models import QuerySet, query
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from generic_reponse import error_response, failed_response, success_response
from .models import  Store
from .serializers import StoreSerializer
from accounts.permissions import IsManager, IsStaff
from .permissions import IsVendor, IsOwnerVendor


class StoreViewSet(GenericAPIView):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsVendor]

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():

                serializer.save(vendor=request.user)

                return success_response(
                    message="Store created successfully",
                    data=serializer.data,
                    status_code=status.HTTP_201_CREATED
                )
            else:
                error_dict = serializer.errors
                first_field = next(iter(error_dict))  # Gets 'mobile'
                error_message = error_dict[first_field][0]  # Gets the first string in the list

                return error_response(
                    message=error_message,
                    status_code=startus.HTTP_400_BAD_REQUEST,
                    data=None # Or {} if you want to keep the data key empty
                )

        except Exception as e:
            print("STORE CREATE ERROR:", e)
            return failed_response(
                message="Internal server error",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def get(self, req):
        try:
            store = Store.objects.all() 
            
           
            ser = self.serializer_class(store, many=True)
            
            return success_response(
                message="Store list",
                status_code=200,
                data=ser.data
            )
        except Exception as e:
            return error_response(
                # 4. Use str(e) to ensure the error message is serializable
                message=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetStore(GenericAPIView):
    serializer_class = StoreSerializer
    queryset = Store

    def get(self,req):
        try:
            store = QuerySet.objects.all()
            ser = self.serializer_class(data=store)
            return success_response(
                message="Store list",
                status_code = 200,
                data= ser.data
            )
        except Exception as e:
            return error_response(
                message=e,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )