# System
import requests
# Local
from utils.melipayamak import Api

username = '09153171983'
password = 'm$X8!83g$ifchQ5SN!eT'
api = Api(username, password)
sms = api.sms('soap')
URL = "https://rest.payamak-panel.com/api/SendSMS/BaseServiceNumber"


class WSC:  # 0;1;2;3;4;5
    LOGIN_OTP = 108172  # otp
    CONFIRM_PHONE_OTP = 108868  # otp
    WELCOME_REGISTER = 108014  # name
    WITHDRAW_OTP = 112531  # otp
    ORDER_REGISTER = 115191  # type, id
    ORDER_PAYMENT = 115189  # type, id, ref


def return_status(value, error_type):
    match error_type:
        case "general":
            switch = {
                '0': 'ارسال شده به مخابرات',
                '1': 'رسیده به مقصد',
                '2': 'نرسیده به مقصد',
                '3': 'خطای مخابراتی',
                '5': 'خطای نامشخص',
                '8': 'رسیده به مخابرات',
                '16': 'نرسیده به مخابرات',
                '35': 'لیست سیاه',
                '100': 'نامشخص',
                '200': 'ارسال شده',
                '300': 'فیلتر شده',
                '400': 'در لیست ارسال',
                '500': 'عدم پذیرش',
            }
            return switch.get(value, 'خطای تعریف نشده')
        case "send_sms":
            switch = {
                "-6": "خطای داخلی رخ داده است با پشتیبانی تماس بگیرید.",
                "-5": "متن ارسالی با توجه به متغیر های مشخص شده در متن پیشفرض همخوانی ندارد.",
                "-4": "کد متن ارسالی صحیح نمی باشد و یا توسط مدیر سامانه تایید نشده است.",
                "-3": "خط ارسالی در سیستم تعریف نشده است، با پشتیبانی سامانه تماس بگیرید",
                "-2": "محدودیت تعداد شماره، محدودیت هر بار ارسال 1 شماره موبایل می باشد.",
                "-1": "دسترسی برای استفاده از این وب سرویس غیر فعال است، با پشتیبانی تماس بگیرید.",
                "0": "نام کاربری یا رمز عبور اشتباه است",
                "1": "پیامک با موفقیت ارسال شد",
                "2": "اعتبار کافی نمی باشد",
                "3": "محدودیت در ارسال روزانه",
                "4": "محدودیت در حجم ارسال",
                "5": "شماره فرستنده معتبر نمی باشد",
                "6": "سامانه در حال بروزرسانی می باشد",
                "7": "متن پیامک حاوی کلمات غیر مجاز است",
                "9": "ارسال از طریق وب سرویس امکان پذیر نیست",
                "10": "کاربر مورد نظر فعال نمی باشد",
                "11": "ارسال نشده",
                "12": "مدارک کاربر کامل نمی باشد",
            }
            return switch.get(value, "خطای تعریف نشده")
        case _:
            return f'خطای تعریف نشده، لطفا با تیم پشتیبانی تماس حاصل فرمایید، {value}'


def send_pattern_sms(text, to, body_id):
    response = requests.post(URL, data={
        'username': username,
        'password': password,
        'text': text,
        'to': to,
        'bodyId': body_id
    })

    return response
