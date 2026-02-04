from rest_framework.response import Response
from rest_framework.views import status



def success_response(message, data=None,status_code=status.HTTP_200_OK):
    return Response({
        'statusCode': status_code,
        "success": True,
        "hasError": False,
        "message": message,
        "data": data
    })

def error_response(message, data=None,status_code=status.HTTP_400_BAD_REQUEST):
    return Response({
        'statusCode': status_code,
        "success": False,
        "hasError": True,
        "message": message,
        "data": data
    })

def failed_response(message="Something went wrong", data=None,):
    return Response({
        'statusCode': 500,
        "success": False,
        "hasError": True,
        "message": message,
        "data": data
    })