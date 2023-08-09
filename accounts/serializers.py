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
    # full_name_persian = serializers.CharField(source='get_full_name_persian')
    # full_name_english = serializers.CharField(source='get_full_name_english')
    birthdate_persian = serializers.CharField(source='get_birthdate_persian', read_only=True)
    passport_expiry_date_persian = serializers.CharField(source='get_passport_expiry_date_persian', read_only=True)

    class Meta:
        model = models.User
        exclude = ('password',)


class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'balance', 'income', 'spend')


class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserTransaction
        fields = '__all__'

