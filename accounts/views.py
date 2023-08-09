import jdatetime
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
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
    queryset = models.UserTransaction.objects.all()


class UserWalletRetrieveView(generics.RetrieveAPIView):
    serializer_class = serializers.UserWalletSerializer
    queryset = models.User.objects.all()