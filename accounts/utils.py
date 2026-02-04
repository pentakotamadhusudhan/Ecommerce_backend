from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "statusCode": response.status_code,
            "success": False,
            "hasError": True,
            "message": "Validation error",
            "data": response.data
        }, status=response.status_code)

    return Response({
        "statusCode": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "success": False,
        "hasError": True,
        "message": "Internal server error",
        "data": None
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
