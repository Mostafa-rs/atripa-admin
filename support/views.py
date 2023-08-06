from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView,\
                                    UpdateAPIView
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

    def get(self, request, *args, **kwargs):
        filters = request.query_params.get('filters')
        qs = self.get_queryset()
        if '/' in filters:
            i = filters.index('/')
            filters = filters[:i] + filters[i+1:]
        if filters:
            if filters == 'waiting':
                qs = qs.filter(viewer=None).exclude(closed=True)
            elif filters == 'me':
                qs = qs.filter(viewer=request.user).exclude(closed=True)
            elif filters == 'others':
                qs = qs.exclude(viewer=request.user).exclude(viewer=None).exclude(closed=True)
            elif filters == 'closed':
                qs = qs.filter(closed=True)
            else:
                qs = qs.exclude(viewer=None)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


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


class SupportAdminChatCreateView(CreateAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatCreateSerializer

    def create(self, request, *args, **kwargs):
        supp = models.Support.objects.get(pk=kwargs['pk'])
        instance = models.Chat.objects.create(support=supp, sender=request.user, receiver=supp.creator,
                                              message=request.data['message'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SupportChatsListView(ListAPIView):
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        return models.Chat.objects.filter(support_id=self.kwargs['pk'])


class SupportAssignToAdminView(UpdateAPIView):
    queryset = models.Support.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewer = request.user
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SupportCloseView(UpdateAPIView):
    queryset = models.Support.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.closed = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



