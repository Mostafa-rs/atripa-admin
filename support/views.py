from django.shortcuts import render
from . import models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers
from rest_framework.exceptions import APIException


class SupportListCreateView(ListCreateAPIView):
    queryset = models.Support.objects.all()
    serializer_class = serializers.SupportSerializer

    def perform_create(self, serializer):
        subjects = self.request.POST.get('subjects')
        if len(subjects) > 2:
            raise APIException({'detail': "Can't assign more than 2 subjects!"})
        instance = serializer.save()
        instance.ip = self.request.POST.get('ip')
        instance.save()
        for sub in subjects:
            instance.subjects.add(sub)


class SupportRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Support.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        qs = super().get_object()
        subjects = self.request.data.get('subjects')
        if subjects:
            if qs.subjects.all().count() == 2:
                raise APIException({'error': "This support already has 2 subjects. can't assign more!"})
        return super().update(request, *args, **kwargs)
