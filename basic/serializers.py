"""
سریالایزر دیتا اپلیکیشن اطلاعات پایه
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""

from rest_framework import serializers
from . import models


class ContinentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Continental
        fields = ('id', 'name')


class PrefixNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrefixNumber
        fields = ('id', 'number')


class CountrySerializer(serializers.ModelSerializer):
    continental = serializers.StringRelatedField(source='continental.name')
    prefix_number = serializers.StringRelatedField(source='prefix_number.number')

    class Meta:
        model = models.Country
        fields = ('id', 'name', 'english_name', 'prefix_number', 'iata', 'description', 'continental_id', 'continental',
                  'prefix_number_id')


class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = models.Province
        fields = ('id', 'name', 'english_name', 'country', 'description')


class CitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    # country = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = models.City
        fields = ('id', 'name', 'english_name', 'province', 'country', 'is_country_capital', 'is_province_capital',
                  'iata', 'latitude', 'longitude')


class TerminalSerializer(serializers.ModelSerializer):
    terminal_type = serializers.CharField(source='get_type', read_only=True)
    province = serializers.CharField(source='province.name', read_only=True)
    country = serializers.CharField(source='country.name', read_only=True)
    city = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model = models.Terminal
        fields = ('id', 'name', 'english_name', 'terminal_type', 'country', 'province', 'city', 'popularity', 'iata',
                  'is_international', 'type', 'longitude', 'latitude', 'address', 'description')


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = serializers.CharField(source='get_type', read_only=True)

    class Meta:
        model = models.Vehicle
        fields = '__all__'


class AccommodationFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccommodationFeature
        fields = '__all__'


class AccommodationRoomSerializer(serializers.ModelSerializer):
    features = AccommodationFeatureSerializer(read_only=True, many=True)

    class Meta:
        model = models.AccommodationRoom
        fields = '__all__'


class AccommodationSerializer(serializers.ModelSerializer):
    accommodation_type = serializers.CharField(source='get_type', read_only=True)
    # bar_accommodation = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    bar_accommodation = AccommodationRoomSerializer(many=True, read_only=True)
    room_counts = serializers.IntegerField(source='room_count', read_only=True)
    province = serializers.CharField(source='province.name', read_only=True)
    province_id = serializers.CharField(source='province.id', read_only=True)
    country = serializers.CharField(source='country.name', read_only=True)
    country_id = serializers.IntegerField(source='country.id', read_only=True)
    city = serializers.CharField(source='city.name', read_only=True)
    city_id = serializers.CharField(source='city.id', read_only=True)
    features = AccommodationFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = models.Accommodation
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = '__all__'


class SubscribeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscribeOptions
        fields = ('id', 'name',)


class SubscribeSerializer(serializers.ModelSerializer):
    # bso_subscribe = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    bso_subscribe = SubscribeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Subscribe
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    father = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = models.SupportType
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'
