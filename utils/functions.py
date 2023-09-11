# System
import os
import re
import requests
import uuid
from datetime import datetime, timedelta, date
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible
# Local
from main.settings import MEDIA_ROOT
from reserve.models import AgeGroup


@deconstructible
class RenamePathFile(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = str(uuid.uuid4()) + '.' + ext
        return os.path.join(self.path, filename)


def format_number(num):

    if num % 1 == 0:
        return int(num)

    else:
        return num


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_device(request):
    device = ''
    device += f'{request.user_agent.device.family} - '
    device += f'({request.user_agent.os.family}-{request.user_agent.os.version_string}) - '
    device += f'({request.user_agent.browser.family}-{request.user_agent.browser.version_string})'

    return device


def check_validation(value, vld):
    """
        تابع بررسی مقدار های ورودی
    """
    match vld:
        case "phone_number":
            return True if len(value) == 11 and value[:2] == "09" else False
        case "username":
            return True if re.match(r"[A-Za-z0-9]", value) else False
        case "persian":
            return True if len(value) >= 2 and re.match(r"^[\u0600-\u06FF\s]+$", value) else False
        case "password":
            return True if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", value) else False
        case "_":
            return False
    return False


def create_expiration(time, extra_secs):
    """
        تابع ساخت تاریخ انقضا
    """
    full_date = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
    full_date += timedelta(seconds=extra_secs)
    return full_date


def check_location_open_hours(saturday, sunday, monday, tuesday, wednesday, thursday, friday, holiday):
    _open_hours = {}
    if saturday is not None:
        match saturday:
            case "0":
                _open_hours['saturday'] = 'تعطیل'
            case "9999":
                _open_hours['saturday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(saturday) == 9:
                    _open_hours['saturday'] = f'{saturday[0:2]}:{saturday[2:4]}-{saturday[5:7]}:{saturday[7:9]}'
                elif len(saturday) == 19:
                    _open_hours['saturday'] = f'{saturday[0:2]}:{saturday[2:4]}-{saturday[5:7]}:{saturday[7:9]} / ' \
                                          f'{saturday[10:12]}:{saturday[12:14]}-{saturday[15:17]}:{saturday[17:19]}'
    if sunday is not None:
        match sunday:
            case "0":
                _open_hours['sunday'] = 'تعطیل'
            case "9999":
                _open_hours['sunday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(sunday) == 9:
                    _open_hours['sunday'] = f'{sunday[0:2]}:{sunday[2:4]}-{sunday[5:7]}:{sunday[7:9]}'
                elif len(sunday) == 19:
                    _open_hours['sunday'] = f'{sunday[0:2]}:{sunday[2:4]}-{sunday[5:7]}:{sunday[7:9]} / ' \
                        f'{sunday[10:12]}:{sunday[12:14]}-{sunday[15:17]}:{sunday[17:19]}'
    if monday is not None:
        match monday:
            case "0":
                _open_hours['monday'] = 'تعطیل'
            case "9999":
                _open_hours['monday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(monday) == 9:
                    _open_hours['monday'] = f'{monday[0:2]}:{monday[2:4]}-{monday[5:7]}:{monday[7:9]}'
                elif len(monday) == 19:
                    _open_hours['monday'] = f'{monday[0:2]}:{monday[2:4]}-{monday[5:7]}:{monday[7:9]} / ' \
                        f'{monday[10:12]}:{monday[12:14]}-{monday[15:17]}:{monday[17:19]}'
    if tuesday is not None:
        match tuesday:
            case "0":
                _open_hours['tuesday'] = 'تعطیل'
            case "9999":
                _open_hours['tuesday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(tuesday) == 9:
                    _open_hours['tuesday'] = f'{tuesday[0:2]}:{tuesday[2:4]}-{tuesday[5:7]}:{tuesday[7:9]}'
                elif len(tuesday) == 19:
                    _open_hours['tuesday'] = f'{tuesday[0:2]}:{tuesday[2:4]}-{tuesday[5:7]}:{tuesday[7:9]} / ' \
                        f'{tuesday[10:12]}:{tuesday[12:14]}-{tuesday[15:17]}:{tuesday[17:19]}'
    if wednesday is not None:
        match wednesday:
            case "0":
                _open_hours['wednesday'] = 'تعطیل'
            case "9999":
                _open_hours['wednesday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(wednesday) == 9:
                    _open_hours['wednesday'] = f'{wednesday[0:2]}:{wednesday[2:4]}-{wednesday[5:7]}:{wednesday[7:9]}'
                elif len(wednesday) == 19:
                    _open_hours['wednesday'] = f'{wednesday[0:2]}:{wednesday[2:4]}-{wednesday[5:7]}:{wednesday[7:9]} /'\
                        f' {wednesday[10:12]}:{wednesday[12:14]}-{wednesday[15:17]}:{wednesday[17:19]}'
    if thursday is not None:
        match thursday:
            case "0":
                _open_hours['thursday'] = 'تعطیل'
            case "9999":
                _open_hours['thursday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(thursday) == 9:
                    _open_hours['thursday'] = f'{thursday[0:2]}:{thursday[2:4]}-{thursday[5:7]}:{thursday[7:9]}'
                elif len(thursday) == 19:
                    _open_hours['thursday'] = f'{thursday[0:2]}:{thursday[2:4]}-{thursday[5:7]}:{thursday[7:9]} / ' \
                        f'{thursday[10:12]}:{thursday[12:14]}-{thursday[15:17]}:{thursday[17:19]}'
    if friday is not None:
        match friday:
            case "0":
                _open_hours['friday'] = 'تعطیل'
            case "9999":
                _open_hours['friday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(friday) == 9:
                    _open_hours['friday'] = f'{friday[0:2]}:{friday[2:4]}-{friday[5:7]}:{friday[7:9]}'
                elif len(friday) == 19:
                    _open_hours['friday'] = f'{friday[0:2]}:{friday[2:4]}-{friday[5:7]}:{friday[7:9]} / ' \
                                          f'{friday[10:12]}:{friday[12:14]}-{friday[15:17]}:{friday[17:19]}'
    if holiday is not None:
        match holiday:
            case "0":
                _open_hours['holiday'] = 'تعطیل'
            case "9999":
                _open_hours['holiday'] = '00:00-23:59'
            case None:
                _open_hours['saturday'] = 'تعریف نشده'
            case _:
                if len(holiday) == 9:
                    _open_hours['holiday'] = f'{holiday[0:2]}:{holiday[2:4]}-{holiday[5:7]}:{holiday[7:9]}'
                elif len(holiday) == 19:
                    _open_hours['holiday'] = f'{holiday[0:2]}:{holiday[2:4]}-{holiday[5:7]}:{holiday[7:9]} / ' \
                                          f'{holiday[10:12]}:{holiday[12:14]}-{holiday[15:17]}:{holiday[17:19]}'

    return _open_hours


def check_location_months(value):
    """
        تابع بررسی ماه های فارسی
    """
    month = ''
    if value == '111111111111':
        return "تمام سال"
    if value == "000000000000":
        return ""

    if value[0:3] == "111":
        month += 'بهار'
    else:
        if value[0] == '1':
            month += 'فروردین، '
        if value[1] == '1':
            month += 'اردیبهشت، '
        if value[2] == '1':
            month += 'خرداد، '

    if value[3:6] == "111":
        month += 'تابستان'
    else:
        if value[3] == '1':
            month += 'تیر، '
        if value[4] == '1':
            month += 'مرداد، '
        if value[5] == '1':
            month += 'شهریور، '

    if value[6:9] == "111":
        month += 'پاییز'
    else:
        if value[6] == '1':
            month += 'مهر، '
        if value[7] == '1':
            month += 'آبان، '
        if value[8] == '1':
            month += 'آذر، '

    if value[9:12] == "111":
        month += 'زمستان'
    else:
        if value[9] == '1':
            month += 'دی، '
        if value[10] == '1':
            month += 'بهمن، '
        if value[11] == '1':
            month += 'اسفند'

    return month


def save_uploaded_file(file, path):
    if file is None or path is None:
        return None
    _path = MEDIA_ROOT + path
    _fss = FileSystemStorage(location=_path)
    _ext = file.name.split('.')[-1]
    _name = f'{str(uuid.uuid4())}.{_ext}'
    _file = _fss.save(_name, file)
    _file_url = _fss.url(path + _file)
    return _file_url


def save_url_file(url, path):
    if url is None or path is None:
        return None

    response = requests.get(url)

    if response.status_code == 200:
        new_path = MEDIA_ROOT + path
        fss = FileSystemStorage(location=new_path)
        ext = url.split('.')[-1]
        name = f'{str(uuid.uuid4())}.{ext}'

        with fss.open(name, 'wb') as file:
            file.write(response.content)

        file_url = fss.url(path + name)
        return file_url

    else:
        return None


def remove_file(path):
    _file = path.split("/")[-1]
    _file_path = os.path.join(MEDIA_ROOT + path[6:-len(_file)], _file)
    os.remove(_file_path)


def calc_age_group(birthdate):
    today = date.today()
    _birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - _birthdate.year - ((today.month, today.day) < (_birthdate.month, _birthdate.day))
    if 0 < age <= 2:
        return AgeGroup.INFANT
    elif 2 < age <= 6:
        return AgeGroup.CHILD
    else:
        return AgeGroup.ADULT


def create_list_from_column(query, column):
    return list(query.values_list(column, flat=True))


def remove_duplicates_from_list(original_list):
    return list(set(original_list))
