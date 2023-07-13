from django.shortcuts import render
from . import models, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
from . import filters as myfilters
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework import status


class CountryListCreateView(ListCreateAPIView):
    serializer_class = serializers.CountrySerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name')))\
                                               .order_by('-id')
            return qs
        return models.Country.objects.all().order_by('-id')


class CountryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class ProvinceListCreateView(ListCreateAPIView):
    serializer_class = serializers.ProvinceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name')))\
                                               .order_by('-id')
            return qs
        return models.Province.objects.all().order_by('-id')


class ProvinceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer


class CityListCreateView(ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.City.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name')),
                                            deleted=False)\
                                               .order_by('-id')
            return qs
        return models.City.objects.filter(deleted=False).order_by('-id')


class CityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.City.objects.filter(deleted=False)
    serializer_class = serializers.CitySerializer
    permission_classes = [AllowAny]
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')

    def delete(self, request, *args, **kwargs):
        if models.City.objects.filter(pk=kwargs['pk']).exists():
            city = models.City.objects.get(pk=kwargs['pk'])
            city.deleted = True
            city.save()
            return JsonResponse({'detail': 'City has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'City not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        instance = models.City.objects.get(pk=kwargs['pk'])
        instance.name = request.data['data']['name']
        instance.save()
        return super().patch(request, *args, **kwargs)
        # instance = models.City.objects.get(pk=kwargs['pk'])
        # instance.name = request.data['name']
        # instance.english_name = request.data['english_name']
        # instance.province = request.data['province']
        # instance.province = request.data['province']
        # instance.country = request.data['country']
        # instance.longitude = request.data['longitude']
        # instance.iata = request.data['iata']
        # instance.latitude = request.data['latitude']
        # instance.latitude = request.data['latitude']


class TerminalListCreateView(ListCreateAPIView):
    serializer_class = serializers.TerminalSerializer

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name'))) \
                                               .order_by('-id')
            return qs
        return models.Terminal.objects.all().order_by('-id')


class TerminalRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Terminal.objects.all()
    serializer_class = serializers.TerminalSerializer


class VehicleListCreateView(ListCreateAPIView):
    queryset = models.Vehicle.objects.all().order_by('-id')
    serializer_class = serializers.VehicleSerializer
    filterset_class = myfilters.VehicleFilter


class VehicleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer


class AccommodationListCreateView(ListCreateAPIView):
    queryset = models.Accommodation.objects.all().order_by('-id')
    serializer_class = serializers.AccommodationSerializer
    filterset_class = myfilters.AccommodationFilter


class AccommodationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer


class BankListCreateView(ListCreateAPIView):
    queryset = models.Bank.objects.all().order_by('-id')
    serializer_class = serializers.BankSerializer
    filterset_class = myfilters.BankFilter


class BankRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.BankSerializer


class SubscribeListCreateView(ListCreateAPIView):
    serializer_class = serializers.SubscribeSerializer

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name'))) \
                                               .order_by('-id')
            return qs
        return models.Subscribe.objects.all()


class SubscribeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Subscribe.objects.all()
    serializer_class = serializers.SubscribeSerializer


class SupportListCreateView(ListCreateAPIView):
    queryset = models.SupportType.objects.all().exclude(father=None).order_by('-id')
    serializer_class = serializers.SupportSerializer
    filterset_class = myfilters.SupportFilter
    

class SupportRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.SupportType.objects.all()
    serializer_class = serializers.SupportSerializer


class CompanyListCreateView(ListCreateAPIView):
    queryset = models.Company.objects.all().order_by('-id')
    serializer_class = serializers.CompanySerializer
    filterset_class = myfilters.CompanyFilter


class CompanyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer



