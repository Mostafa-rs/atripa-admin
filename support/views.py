"""
    Support Serializers
    Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/26
"""

# System
from datetime import datetime
# Third Party
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, status
# from rest_framework import permissions
from rest_framework.response import Response
# Local
from . import serializers, models
from utils.defines import Message
from utils.functions import get_client_ip


class ContactForm(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.ContactFormSerializer

    def post(self, request, *args, **kwargs):
        """
            افزودن فرم ارتباط با ما
        """
        try:
            """
                بررسی اسپم نبودن درخواست
            """
            if models.ContactForm.objects.filter(phone_number=request.data['phone_number']).filter(ip=get_client_ip(
                    request)).filter(date_time__month=datetime.now().month).filter(date_time__day=datetime.now().day)\
                    .exists():
                return Response({"message": Message.ERR_SUP_CONTACT_FORM_DUPLICATE}, status.HTTP_429_TOO_MANY_REQUESTS)

            serializer = serializers.ContactFormSerializer(data=request.data)
            if serializer.is_valid():
                form = serializer.save()
                models.ContactForm.objects.filter(id=form.id).update(
                    date_time=datetime.now(),
                    ip=get_client_ip(request)
                )
                return Response({"message": Message.OK_SUP_REGISTER}, status.HTTP_200_OK)
            else:
                return Response({"message": Message.ERR_QP_REQUIRED}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f'{Message.ERR_TRY}: {e}'})

