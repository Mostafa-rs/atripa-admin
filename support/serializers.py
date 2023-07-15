from rest_framework import serializers
from . import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name', 'is_child')


class SupportSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = models.Support
        fields = ('id', 'creator', 'email', 'phone_number', 'message', 'subjects', 'viewer', 'ip',
                  'modified')
