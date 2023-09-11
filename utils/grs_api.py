"""
    GRS Accommodation API
    Author: Alireza Rahimi
    Email: Absolut.alireza@gmail.com
    Last Modified: 2023-06-22
    """

import time
import requests
from datetime import datetime, timedelta
from django.core.cache import cache

from basic.models import City, Accommodation, AccommodationImage, AccommodationFeature, AccommodationRoom, Country
from utils.functions import save_url_file

GRS_TOKEN = 'https://api.grschannel.com-$2y$10$ehstnzLUPlVRofKvcAWM1ed'
GRS_URL = 'https://api.grschannel.com/v1'


def get_city_hotel_list(id, check_in, check_out, adults_count, accommodation=None):
    response = cache.get(f'flight_{id}_{check_in}_{check_out}_{adults_count}_{accommodation}')

    if response is None:
        url = GRS_URL + '/suggestion'
        city = City.objects.filter(id=id).first()
        params = {
            'city_id': city.grs_id,
            'check_in': check_in,
            'check_out': check_out,
            'adults_count': adults_count
        }

        if accommodation is not None:
            params['filters[0][operand]'] = 'IsEqualTo'
            params['filters[0][name]'] = 'id'
            params['filters[0][value]'] = accommodation

        headers = {
            'Content-Type': 'application/json',
            'Client-Token': GRS_TOKEN}

        response = requests.get(url, params, headers=headers)

        cache.set(f'flight_{id}_{check_in}_{check_out}_{adults_count}_{accommodation}', response, 180)

    return response


def get_hotel_list():
    for city in City.objects.filter(grs_id__gt=0, id__gt=1070).order_by('id'):
        url = f'{GRS_URL}/properties'
        params = {
            'filters[0][operand]': 'IsEqualTo',
            'filters[0][name]': 'city_id',
            'filters[0][value]': city.grs_id
        }
        headers = {
            'Content-Type': 'application/json',
            'Client-Token': GRS_TOKEN
        }
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for row in data['value']['properties']:
                if Accommodation.objects.filter(grs_id=row['id']).exists():
                    accommodation = Accommodation.objects.filter(grs_id=row['id']).first()

                else:
                    accommodation = Accommodation(
                        name=row['name'],
                        location=str(row['latitude']) + ',' + str(row['longitude']),
                        type=row['type'],
                        country=city.country,
                        province=city.province,
                        city=city,
                        address=row['address'],
                        star=0 if row['star'] is None else row['star'],
                        star_rating=row['score'],
                        latitude=0 if row['latitude'] is None else row['latitude'],
                        longitude=0 if row['longitude'] is None else row['longitude'],
                        description=row['description'],
                        grs_id=row['id'])
                    accommodation.save()

                image_counter = AccommodationImage.objects.filter(accommodation=accommodation).count()
                for image in row['images']:
                    if not AccommodationImage.objects.filter(grs_name=image['name']).exists() and image_counter < 5:
                        AccommodationImage(
                            accommodation=accommodation,
                            image=save_url_file(image['url'], '/basic/accommodation/'),
                            alt=accommodation.name,
                            grs_name=image['name'],
                            caption=image['caption']).save()
                        time.sleep(2)
                        image_counter += 1

                facilities = []
                for facility in row['facilities']:
                    if not Accommodation.objects.filter(id=accommodation.id, features=int(facility['id'])).exists():
                        facilities.append(AccommodationFeature.objects.filter(id=facility['id']).first())

                if facilities is not None:
                    accommodation.features.add(*facilities)

                room_url = GRS_URL + '/room-types'
                room_params = {'property_id': row['id']}
                room_res = requests.get(room_url, params=room_params, headers=headers)

                if room_res.status_code == 200:
                    room_data = room_res.json()

                    for room in room_data['value']['room_types']:
                        if AccommodationRoom.objects.filter(grs_id=room['id']).exists():
                            lroom = AccommodationRoom.objects.filter(grs_id=room['id']).first()

                        else:
                            lroom = AccommodationRoom(
                                accommodation=accommodation,
                                grs_id=room['id'],
                                name=room['name'],
                                type=room['type'],
                                capacity=room['capacity'],
                                extra_capacity=room['extra_capacity'],
                                single_bed_count=room['single_bed_count'],
                                double_bed_count=room['double_bed_count'],
                                sofa_bed_count=room['sofa_bed_count'],
                                out_of_service=True if room['out_of_service'] == 1 else False,
                                accept_child=room['accept_child'],
                                description=room['description'],
                                deleted_at=room['deleted_at'])
                            lroom.save()

                        facilities = []
                        for facility in row['facilities']:
                            if not AccommodationRoom.objects.filter(id=lroom.id, features=int(facility['id'])).exists():
                                facilities.append(AccommodationFeature.objects.filter(id=facility['id']).first())

                        if facilities is not None:
                            lroom.features.add(*facilities)


def get_available_room(id, check_in, check_out):
    url = GRS_URL + '/available-rooms'
    # check_out = datetime.strptime(check_out, '%Y-%m-%d').date() - timedelta(days=1)
    params = {
        'property_id': id,
        'check_in': check_in,
        'check_out': check_out}
    headers = {
        'Content-Type': 'application/json',
        'Client-Token': GRS_TOKEN}

    response = requests.get(url, params, headers=headers)

    return response


def pre_reserve_room(request, data, accommodation, code):
    rooms = []
    for room in data['rooms']:
        country = Country.objects.filter(id=room['country']).first()
        rooms.append({
            'room_type_id': room['id'],
            'rate_plan_id': room['rate_plan_id'],
            'count': 1,
            'adult_count': room['adult'],
            'children': room['children'],
            'guest_first_name': room['first_name'],
            'guest_last_name': room['last_name'],
            'guest_phone': room['phone_number'],
            'guest_email': room['email'],
            'guest_national_code': room['national_code'],
            'guest_passport_number': room['passport_number'],
            'guest_country_id': country.grs_id,
            'guest_city_id': None
        })

    url = GRS_URL + '/reserve'
    body = {
        'property_id': accommodation.grs_id,
        'check_in': data['check_in'],
        'check_out': data['check_out'],
        'booker_first_name': request.user.first_name,
        'booker_last_name': request.user.last_name,
        'booker_phone': request.user.phone_number,
        'booker_email': request.user.email,
        'agency_confirmation_code': code,
        'vehicle': None,
        'vehicle_number': None,
        'description': None,
        'rooms': rooms
    }
    headers = {
        'Content-Type': 'application/json',
        'Client-Token': GRS_TOKEN}

    response = requests.post(url, json=body, headers=headers)

    return response


def book_room(code):
    url = GRS_URL + '/book'
    body = {
        'confirmation_code': code}
    headers = {
        'Content-Type': 'application/json',
        'Client-Token': GRS_TOKEN}

    response = requests.post(url, json=body, headers=headers)

    return response


def get_room_type(type):
    match type:
        case 'adjacent_rooms': return 'سوئیت'
        case 'adjoining_rooms': return 'سوئیت'
        case 'connecting_rooms': return 'کانکت'
        case 'double': return 'دو تخته دبل'
        case 'double_double': return 'چهار تخته دبل'
        case 'king': return 'شاه نشین'
        case 'master_suite': return 'سوئیت رویال'
        case 'mini_suite': return 'سوئیت لوکس'
        case 'quad': return 'چهار تخته کانکت'
        case 'queen': return 'سوئیت کوئین'
        case 'single': return 'یک تخته'
        case 'studio': return 'آپارتمان'
        case 'triple': return 'سه تخته'
        case 'twin': return 'توئین'
        case _: return type
