from rest_framework import serializers

import accounts.serializers
# from accounts import models as accounts_models
from . import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name', 'is_child')


class SupportSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    viewer = serializers.StringRelatedField(source='viewer.full_name')
    creator = serializers.StringRelatedField(source='creator.get_full_name_persian')

    class Meta:
        model = models.Support
        fields = ('id', 'creator', 'email', 'phone_number', 'message', 'subjects', 'viewer', 'ip',
                  'modified', 'get_subjects', 'date_time', 'date_time_persian', 'modified_persian')


# class UserChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = accounts_models.User
#         fields = ('id', 'full_name', 'is_admin')


class ChatSerializer(serializers.ModelSerializer):
    sender = accounts.serializers.UserRetrieveSerializer(read_only=True)
    receiver = accounts.serializers.UserRetrieveSerializer(read_only=True)

    class Meta:
        model = models.Chat
        fields = ('id', 'message', 'sent_at_persian', 'support', 'sender', 'receiver')


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'
