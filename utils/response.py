"""
    API Response Manager
    Author: Alireza Rahimi
    Email: Absolut.alireza@gmail.com
    Last Update: 2023-05-31
    """
import json

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response


def get_response(data=None, message=None, errors=None):

    if errors and len(errors) > 0 and message is None:
        message = 'Error acquired'
    
    elif message is None:
        message = 'Success'

    if errors is not None:
        return Response({
            'message': message,
            'errors': errors,
            'data': None
        }, status=HTTP_400_BAD_REQUEST)
    
    else:
        return Response({
            'message': message,
            'errors': None,
            'data': data
        }, status=HTTP_200_OK)
