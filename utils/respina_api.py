"""
    Respina Flight API
    Author: Alireza Rahimi
    Email: Absolut.alireza@gmail.com
    Last Modified: 2023-06-22
    """

# Third Party
import requests
from django.core.cache import cache
from basic.models import Country

URL = 'https://respina24.ir/'
KEY = 'respina24'
TOKEN = '3e8bcb42a3e29205c4cebbdf390dae86'
USER = '09153171983'
PASSWORD = '272813'


def get_flight(departure, destination, date):
    response = cache.get(f'flight_{date}_{departure}_{destination}')

    if response is None:
        url = URL + 'flight/Availability'
        body = {
            'departureDate': date,
            'from': departure,
            'to': destination
        }
        headers = {
            'respina24': 'respina24',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=body, headers=headers)

        cache.set(f'flight_{date}_{departure}_{destination}', response, 180)
    
    return response


def reserve_flight(request, data):
    url = URL + 'flight/Book'
    flight_info = {
            'id': data['id'],
            'capacity': data['capacity'],
            'aircraft': data['aircraft'],
            'cobin': data['cobin'],
            'type': data['type'],
            'refundable': data['refundable'],
            'adultPrice': data['adult_price'],
            'childPrice': data['child_price'],
            'infantPrice': data['infant_price'],
            'airlineName': data['airline'],
            'airelineNamePersian': data['airline_persian'],
            'airlineLogo': data['airline_logo'],
            'flightNumber': data['flight_number'],
            'from': data['departure'],
            'fromFa': data['departure_name'],
            'departureTime': data['departure_time'],
            'from_airport_name': data['departure_terminal'],
            'to': data['destination'],
            'toFa': data['destination_name'],
            'arrivalTime': data['destination_time'],
            'to_airport_name': data['destination_terminal'],
            'flightDuration': data['flight_duration'],
            'cobinPersian': data['cobin_persian'],
            'departureDate': data['departure_date'],
            'class': data['class']
        }
    passengers = []

    for row in data['passengers']:

        if row['country'] is None or row['country'] == 1:
            country = 'IRN'
        else:
            country = Country.objects.filter(id=row['country']).first()['nationality']

        passengers.append({
            'passengerType': row['passenger_type'],
            'birthday': row['birthday'],
            'passengerName': {
                'persianFirstName': row['first_name'],
                'persianLastName': row['last_name'],
                'englishFirstName': row['first_name_en'],
                'englishLastName': row['last_name_en']
            },
            'gender': row['gender'],
            'nationalityId': row['national_code'],
            'PassportNumber': row['passport_number'],
            'nationalityCode': country
        })

    body = {
        'flightInfo': flight_info,
        'mobile': '09153171983',
        'email': 'info@atripa.ir',
        'captcha-flight': '',
        'os': 'IPHONE',
        'travelerInfo': passengers}
    headers = {
        'Content-Type': 'application/json',
        'respina24': 'respina24'
    }
    response = requests.post(url, json=body, headers=headers)

    return response


def book_flight(code):
    url = URL + 'flight/Order'
    body = {
        'POS': {
            'appKey': KEY,
            'appSecret': TOKEN
        },
        'UserInfo': {
            'Cellphone': USER,
            'Password': PASSWORD
        },
        'ReservationId': code}
    response = requests.post(url, json=body)

    return response
