import requests

SAMAN_TERMINAL = 13158592

SEP_VERIFY_NOT_FOUND = -2  # تراکنش یافت نشد.
SEP_VERIFY_EXPIRED = -6  # بیش از نیم ساعت از زمان اجرای تراکنش گذشته است
SEP_VERIFY_OK = 0  # عملیات با موفقیت انجام شد
SEP_VERIFY_DUPLICATE = 2  # درخواست تکراری می باشد.
SEP_VERIFY_TERMINAL_NOT_FOUND = -105  # ترمینال ارسالی در سیستم موجود نمی باشد
SEP_VERIFY_TERMINAL_DISABLE = -104  # ترمینال ارسال ی غیر فعال می باشد
SEP_VERIFY_IP_INVALID = -106  # آدرس آی پی درخواستی غیر مجاز می باشد


def get_saman_get_token(user, amount, tracking_id, terminal=None):
    _terminal = SAMAN_TERMINAL
    _response = requests.post(
        url="https://sep.shaparak.ir/onlinepg/onlinepg",
        json={
            "action": "token",
            "TerminalId": _terminal,
            "Amount": amount,
            "ResNum": tracking_id,
            "RedirectUrl": "https://api.atripa.com/reserve/payment_result/",
            "CellNumber": user.phone_number
        })
    return _response


def post_saman_verify_payment(reference_number, terminal_id):
    _response = requests.post(
        url="https://sep.shaparak.ir/verifyTxnRandomSessionkey/ipg/VerifyTransaction",
        json={
            "RefNum": reference_number,
            "TerminalNumber": terminal_id
        })
    return _response


def get_saman_errors(type, error):
    match type:
        case "afterPayment":
            match error:
                case 1:
                    return "کاربر انصراف داده است"
                case 2:
                    return "پرداخت با موفقیت انجام شد"
                case 3:
                    return "پرداخت انجام نشد."
                case 4:
                    return "کاربر در بازه زمانی تعیین شده پاسخی ارسال نکرده است."
                case 5:
                    return "پارامترهای ارسالی نامعتبر است."
                case 8:
                    return "آدرس سرور پذیرنده نامعتبر است (در پرداخت های بر پایه توکن)"
                case 10:
                    return "توکن ارسال شده یافت نشد"
                case 11:
                    return "با این شماره ترمینال فقط تراکنش های توکنی قابل پرداخت هستند."
                case 12:
                    return "شماره ترمینال ارسال شده یافت نشد."
                case _:
                    return "نامشخص"
        case _:
            return "نامشخص"
