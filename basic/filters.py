from django_filters import rest_framework as filters
from . import models


class VehicleFilter(filters.FilterSet):
    type = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = models.Vehicle
        fields = ('type',)


class AccommodationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Accommodation
        fields = ('name',)


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Bank
        fields = ('name',)


class SupportFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.SupportType
        fields = ('name',)


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Company
        fields = ('name',)