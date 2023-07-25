from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models, serializers


class RewardListCreateView(ListCreateAPIView):
    queryset = models.Reward.objects.all()
    serializer_class = serializers.RewardListSerializer



