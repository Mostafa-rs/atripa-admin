import jdatetime
from rest_framework import generics
from . import serializers, models


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserListSerializer
    queryset = models.User.objects.all()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserRetrieveSerializer
    queryset = models.User.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        b_date = request.data.get('birthdate_persian')
        passport_exp = request.data.get('passport_expiry_date_persian')
        if b_date:
            b_date = b_date.split('-')
            instance.birthdate = jdatetime.date(day=int(b_date[2]), month=int(b_date[1]),
                                                year=int(b_date[0])).togregorian()
            del request.data['birthdate']
        if passport_exp:
            passport_exp = passport_exp.split('-')
            instance.passport_expiry_date = jdatetime.date(day=int(passport_exp[2]), month=int(passport_exp[1]),
                                                           year=int(passport_exp[0])).togregorian()
            del request.data['passport_expiry_date']
        instance.save()

        return super().patch(request, *args, **kwargs)


class UserFinanceListView(generics.ListAPIView):
    serializer_class = serializers.UserTransactionSerializer

    def get_queryset(self):
        return models.UserTransaction.objects.filter(user_id=self.kwargs['pk'])


class UserWalletRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.UserWalletSerializer
    queryset = models.User.objects.all()


class UserBankAccountsListView(generics.ListAPIView):
    serializer_class = serializers.UserBankAccountsSerializer

    def get_queryset(self):
        return models.UserBankAccount.objects.filter(user_id=self.kwargs['pk'], confirmed=True).order_by('-id')


class UserSupportRequestListView(generics.ListAPIView):
    queryset = models.UserSupportRequest.objects.all()
    serializer_class = serializers.SupportRequestSerializer


class UserSupportChatListView(generics.ListAPIView):
    queryset = models.UserSupportChat.objects.all()
    serializer_class = serializers.SupportChatSerializer


class UserFavoriteRetrieveView(generics.RetrieveAPIView):
    queryset = models.UserFavorites.objects.all()
    serializer_class = serializers.UserFavoritesSerializer


class UserSettingsRetrieveView(generics.RetrieveAPIView):
    queryset = models.UserSetting.objects.all()
    serializer_class = serializers.UserSettingsSerializer
