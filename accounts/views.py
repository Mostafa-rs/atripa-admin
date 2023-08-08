from django.shortcuts import render
from rest_framework import generics
from . import serializers, models


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserListSerializer
    queryset = models.User.objects.all()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserRetrieveSerializer
    queryset = models.User.objects.all()
