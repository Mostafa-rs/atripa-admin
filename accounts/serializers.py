from rest_framework import serializers
from . import models


class UserListSerializer(serializers.ModelSerializer):
    subscribe = serializers.SerializerMethodField()
    full_name_persian = serializers.CharField(source='get_full_name_persian')

    def get_subscribe(self, obj):
        return obj.ausu_user.all().last().subscribe.name

    class Meta:
        model = models.User
        exclude = ('password',)


class UserRetrieveSerializer(serializers.ModelSerializer):
    full_name_persian = serializers.CharField(source='get_full_name_persian')
    full_name_english = serializers.CharField(source='get_full_name_english')

    class Meta:
        model = models.User
        exclude = ('password',)


