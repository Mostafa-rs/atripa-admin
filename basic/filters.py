"""
فیلتر دیتا اپلیکیشن اطلاعات پایه
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django_filters import rest_framework as filters
from . import models


class CityFilter(filters.FilterSet):
    D_S = (
        ('0', 'older'),
        ('1', 'newer'),
    )
    A_S = (
        ('0', 'asc alpha'),
        ('1', 'des alpha'),
    )

    # Filter by country
    c_n = filters.ModelMultipleChoiceFilter(queryset=models.Country.objects.all(), field_name='country')
    # Filter by province
    p_n = filters.ModelMultipleChoiceFilter(queryset=models.Province.objects.all(), field_name='province')
    # Filter by is country capital
    c_cap = filters.BooleanFilter(field_name='is_country_capital')
    # Filter by is province capital
    p_cap = filters.BooleanFilter(field_name='is_province_capital')
    # Sort by date
    d_s = filters.ChoiceFilter(choices=D_S, method='d_s_filter')
    # Sort by alphabet
    a_s = filters.ChoiceFilter(choices=D_S, method='a_s_filter')

    def d_s_filter(self, queryset, name, value):
        data = '-id' if value == self.D_S[1][0] else 'id'
        return queryset.order_by(data)

    def a_s_filter(self, queryset, name, value):
        data = '-name' if value == self.A_S[1][0] else 'name'
        return queryset.order_by(data)


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