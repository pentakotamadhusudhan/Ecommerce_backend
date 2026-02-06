from re import S
from django.db import IntegrityError
from django.db.models.base import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from generic_reponse import *

from .models import User
from .serilaizers import LoginSerializer, RegisterSerializer, UserSerializer



class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return success_response(
                    message="User registered successfully",
                    status_code=status.HTTP_201_CREATED,
                    data=serializer.data
                )
            else:
                error_dict = serializer.errors
                first_field = next(iter(error_dict))  # Gets 'mobile'
                error_message = error_dict[first_field][0]  # Gets the first string in the list

                return error_response(
                    message=error_message,
                    status_code=status.HTTP_400_BAD_REQUEST,
                    data=None # Or {} if you want to keep the data key empty
                )
                
        except ValidationError as e:
            return error_response(
                message="Validation error",
                data=e.detail,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        except IntegrityError:
            return error_response(
                message="User already exists",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            print(e)
            return failed_response(message="Internal server error")

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = serializer.validated_data['user']

            return success_response(
                message="Login successful",
                data=UserSerializer(user).data,
                status_code=status.HTTP_200_OK
            )

        except ValidationError as e:
            return error_response(
                message="Invalid credentials",
                data=e.detail,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        except Exception:
            return failed_response(message="Internal server error")




class GetUserView(GenericAPIView):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return success_response(
            message="User details fetched successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )




class GetAllUsersDetails(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return success_response(
            message="All users details fetched successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )
