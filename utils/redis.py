from django.core.cache import cache
from basic.models import City, Accommodation, AccommodationRoom
from basic import models as bm
from location.models import Location


class Key:
    class Admin:
        class Location:
            LIST = 'al_list_cache'

    class Public:
        class Basic:
            COUNTRY_LIST = 'pbc_country_list_cache'
            PROVINCE_LIST = 'pbc_province_list_cache'
            CITY_LIST = 'pbc_city_list_cache'

        class Reserve:
            class Hotel:
                CITY_LIST = 'prh_city_list_cache'
                HOTEL_LIST = 'prh_hotel_list_cache'
                ROOM_LIST = 'prh_room_list_cache'


def set_cache(key):
    data = None

    if cache.get(key) is not None:
        delete_cache(key)

    match key:
        case Key.Admin.Location.LIST:
            data = Location.objects.all().order_by('-id')

        case Key.Public.Basic.COUNTRY_LIST:
            data = bm.Country.objects.all().order_by('id')

        case Key.Public.Basic.PROVINCE_LIST:
            data = bm.Province.objects.all().order_by('id')

        case Key.Public.Basic.CITY_LIST:
            data = bm.City.objects.all().order_by('id')

        case Key.Public.Reserve.Hotel.CITY_LIST:
            data = City.objects.order_by('name')

        case Key.Public.Reserve.Hotel.HOTEL_LIST:
            data = Accommodation.objects.filter(reservable=True)

        case Key.Public.Reserve.Hotel.ROOM_LIST:
            data = AccommodationRoom.objects.all()

        case _:
            data = None

    cache.set(key, data, timeout=86400)
    return data


def set_multi_cache(key, data):
    new_data = None
    time_out = 0

    match key:
        case _:
            new_data = None

    cache.set(f'{key}_{data}', data, timeout=time_out)
    return new_data


def delete_cache(key):
    cache.delete(key)


def get_cache(key, data=None):
    if data is None:
        if cache.get(key) is None:
            return set_cache(key)

        else:
            return cache.get(key)

    elif data is not None:
        if cache.get(f'{key}_{data}') is None:
            return set_multi_cache(key, data)

        else:
            return cache.get(f'{key}_{data}')

    else:
        return None


def delete_group_cache(key):
    match key:
        case _:
            pass
