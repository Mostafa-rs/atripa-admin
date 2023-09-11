from rest_framework import serializers
from . import models
from django.contrib.humanize.templatetags.humanize import intcomma
from basic.serializers import BankSerializer


class UserListSerializer(serializers.ModelSerializer):
    subscribe = serializers.SerializerMethodField()
    full_name_persian = serializers.CharField(source='get_full_name_persian')

    def get_subscribe(self, obj):
        if models.UserSubscribe.objects.filter(user_id=obj.id).exists():
            return obj.ausu_user.all().last().subscribe.name
        return ' '

    class Meta:
        model = models.User
        exclude = ('password',)


class UserRetrieveSerializer(serializers.ModelSerializer):
    birthdate_persian = serializers.CharField(source='get_birthdate_persian', read_only=True)
    passport_expiry_date_persian = serializers.CharField(source='get_passport_expiry_date_persian', read_only=True)

    class Meta:
        model = models.User
        exclude = ('password',)


class UserWalletSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    spend = serializers.SerializerMethodField()
    income = serializers.SerializerMethodField()

    def get_balance(self, obj):
        return intcomma(obj.balance)

    def get_spend(self, obj):
        return intcomma(obj.spend)

    def get_income(self, obj):
        return intcomma(obj.income)

    class Meta:
        model = models.User
        fields = ('id', 'income', 'spend', 'balance')


class UserTransactionSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField(read_only=True)
    type_sign = serializers.BooleanField(source='get_type_sign')

    def get_type(self, obj):
        return obj.get_type

    class Meta:
        model = models.UserTransaction
        fields = '__all__'


class UserBankAccountsSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = models.UserBankAccount
        fields = '__all__'


class SupportChatSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.get_full_name_persian')
    date = serializers.CharField(source='get_date_persian')

    class Meta:
        model = models.UserSupportChat
        fields = '__all__'


class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserFavorites
        fields = '__all__'


class UserSettingsSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = models.UserSetting
        fields = '__all__'


class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPoint
        exclude = ('user', )


class SupportSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.get_full_name_persian', read_only=True)
    supporter = serializers.CharField(source='supporter.get_full_name_persian', read_only=True)
    status = serializers.CharField(source='get_status', read_only=True)
    status_no = serializers.IntegerField(source='status')
    type = serializers.CharField(source='get_type', read_only=True)
    single_type = serializers.CharField(source='type.name')
    modified_persian = serializers.CharField(source='get_last_modified_date_persian', read_only=True)
    register_date_persian = serializers.CharField(source='get_register_date_persian', read_only=True)

    class Meta:
        model = models.UserSupportRequest
        exclude = ('register_date', 'last_modified_date')


class AgencyListSerializer(serializers.ModelSerializer):
    get_status = serializers.CharField(read_only=True)

    class Meta:
        model = models.Agency
        fields = ('id', 'name', 'ceo', 'economic_code', 'phone_number', 'status', 'get_status')


