"""
اینترفیس کد اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, TokenHasReadWriteScope)
    serializer_class = UserSerializer

