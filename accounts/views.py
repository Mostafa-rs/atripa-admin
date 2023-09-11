import datetime

import jdatetime
from rest_framework import generics, views
from rest_framework.response import Response
from django.utils import timezone
from . import serializers, models
from django.db.models import Q


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


class UserFavoriteRetrieveView(generics.RetrieveAPIView):
    queryset = models.UserFavorites.objects.all()
    serializer_class = serializers.UserFavoritesSerializer


class UserSettingsRetrieveView(generics.RetrieveAPIView):
    queryset = models.UserSetting.objects.all()
    serializer_class = serializers.UserSettingsSerializer


# class UserPointRetrieveView(generics.RetrieveAPIView):
#     serializer_class = serializers


class SupportListView(generics.ListAPIView):
    serializer_class = serializers.SupportSerializer

    def get_queryset(self):
        qs = models.UserSupportRequest.objects.all()
        query_param = self.request.query_params.get('qs')
        if query_param:
            if query_param == 'waiting':
                qs = qs.filter(supporter=None)
            if query_param == 'me':
                qs = qs.filter(supporter=self.request.user).exclude(
                    Q(status=models.UserSupportRequest.Status.CLOSED_BY_USER) |
                    Q(status=models.UserSupportRequest.Status.CLOSED_BY_SUPPORT)
                )
            if query_param == 'others':
                qs = qs.exclude(Q(supporter=self.request.user) | Q(supporter=None))
            if query_param == 'closed':
                qs = qs.filter(Q(status=models.UserSupportRequest.Status.CLOSED_BY_USER) |
                               Q(status=models.UserSupportRequest.Status.CLOSED_BY_SUPPORT))
            if query_param == 'qc':
                qs = qs.filter(status=models.UserSupportRequest.Status.COMPLAIN)

            return qs


class UserSupportChatListView(generics.ListAPIView):
    serializer_class = serializers.SupportChatSerializer

    def get_queryset(self):
        qs = models.UserSupportChat.objects.all()
        pk = self.kwargs.get('pk')
        return qs.filter(request_id=pk)


class AdminSupportAccept(generics.UpdateAPIView):
    queryset = models.UserSupportRequest.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.supporter = self.request.user
        obj.save()
        serializer = self.get_serializer(obj)

        return Response(serializer.data)


class SupportCloseChatView(generics.UpdateAPIView):
    queryset = models.UserSupportRequest.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.status = 3
        obj.save()
        serializer = self.get_serializer(obj)

        return Response(serializer.data)


class SupportChatResponseView(generics.CreateAPIView):
    queryset = models.UserSupportChat.objects.all()
    serializer_class = serializers.SupportChatSerializer

    def post(self, request, *args, **kwargs):
        req_pk = self.kwargs.get('pk')
        obj = models.UserSupportChat.objects.create(
            request_id=req_pk,
            user_id=request.user.id,
            type=models.UserSupportChat.Type.SUPPORTER,
            date=timezone.now(),
            attach=request.data.get('attach'),
            text=request.data.get('text')
        )
        ser_data = self.serializer_class(obj).data
        return Response(ser_data)


class AdminsListView(generics.ListAPIView):
    serializer_class = serializers.UserListSerializer

    def get_queryset(self):
        qs = models.User.objects.filter(is_staff=True, is_active=True).exclude(id=self.request.user.id)
        search_query = self.request.query_params.get('search')
        if search_query:
            qs = qs.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) |
                           Q(english_first_name__icontains=search_query) | Q(english_last_name__icontains=search_query)
                           | Q(id__icontains=search_query))

        return qs


class ReassignSupportAdmin(generics.UpdateAPIView):
    queryset = models.UserSupportRequest.objects.all()
    serializer_class = serializers.SupportSerializer

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        new_admin = models.User.objects.get(pk=request.data.get('admin_pk'))
        obj.supporter = new_admin
        obj.save()

        ser_data = self.serializer_class(obj).data

        return Response(ser_data)


class UserSupportsListView(generics.ListAPIView):
    serializer_class = serializers.SupportSerializer

    def get_queryset(self):
        return models.UserSupportRequest.objects.filter(user_id=self.kwargs['pk'])


class AgencyListView(generics.ListAPIView):
    queryset = models.Agency.objects.all()
    serializer_class = serializers.AgencyListSerializer


class NotDeterminedAgenciesCountView(views.APIView):
    def get(self, request, *args, **kwargs):
        res = {
            'count': models.Agency.objects.filter(status=0).count()
        }

        return Response(res)
