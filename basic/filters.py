"""
فیلتر دیتا اپلیکیشن اطلاعات پایه
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django_filters import rest_framework as filters
from . import models


class CityFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='icontains')
    # english_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.City
        fields = ('name', 'english_name')


class VehicleFilter(filters.FilterSet):
    v_type = filters.NumberFilter(lookup_expr='exact', field_name='type')

    class Meta:
        model = models.Vehicle
        fields = ('v_type',)


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