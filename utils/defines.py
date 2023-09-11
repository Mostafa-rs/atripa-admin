class Message:
    """
        Error
    """
    # General
    ERR_QP_REQUIRED = 'اطلاعات ارسالی کامل نیست'
    ERR_PK_REQUIRED = 'شناسه ارسالی صحیح نیست یا در مقادیر وجود ندارد.'
    ERR_TRY = 'خطایی رخ داده است، لطفاً بعداً تلاش نمایید و یا با تیم پشتیبانی تماس حاصل فرمایید.'
    ERR_FILES_NOT_FOUND = 'فایل یا تصویر مورد نیاز بارگذاری نشده است.'
    ERR_FILES_WRONG_FORMAT = 'فایل یا تصویر ارسالی فرمت مناسبی ندارند.'
    ERR_ACCESS_DENIED = 'شما دسترسی لازم برای این فرآیند را ندارید'

    # Authentication
    ERR_REGISTER = 'ثبت نام با خطا مواجه شده است، لطفا مجددا تلاش نمایید.'
    ERR_REGISTER_DUPLICATE = 'شماره تلفن یا نام کاربری تکراری است. لطفا از فراموشی رمز عبور استفاده نمایید.'
    ERR_LOGIN_OTP_EXIST = 'یکبار رمز برای شما ارسال شده است، لطفاً چند دقیقه بعد مجدداً تلاش نمایید.'
    ERR_LOGIN_OTP_EXPIRE = 'یکبار رمز صحیح نیست یا اعتبار آن به اتمام رسیده است، لطفاً مجدداً تلاش نمایید.'

    # Accounts
    ERR_NOT_LOGGED_IN = 'لطفا وارد شوید'
    ERR_ACCOUNT_DOES_NOT_EXIST = 'حساب کاربری مورد نظر وجود ندارد.'
    ERR_OTP_SEND_RECENTLY = 'یکبار رمز به تازگی ارسال شده است، لطفاً بعداً تلاش نمایید.'
    ERR_OTP_EXPIRED = 'یکبار رمز منقضی شده است'
    ERR_OTP_WRONG = 'یکباررمز وارد شده صحیح نمی باشد'
    ERR_PASSWORD_REQUIRED = 'رمز عبور وارد نشده است'
    ERR_NEW_PASSWORD_NOT_MATCH = 'رمز عبور و تکرار آن یکسان نمی باشد'
    ERR_PASSWORD_WRONG = 'رمز عبور اشتباه است'
    ERR_SHOP_CONFIRMED_NO_EDIT = 'فروشگاه تایید شده امکان ویرایش ندارد، لطفا از قسمت پشتیبانی اقدام فرمایید.'
    ERR_COMPANY_CONFIRMED_NO_EDIT = 'اطلاعات حقوقی تایید شده امکان ویرایش ندارد، لطفا از قسمت پشتیبانی اقدام فرمایید.'
    ERR_PASSENGER_NOT_FOUND = 'همسفر پیدا نشد'
    ERR_PASSENGER_DUPLICATE = 'همسفر با این مشخصات وجود دارد'
    ERR_PHONE_VERIFIED = 'تلفن همراه شما تایید شده است'
    ERR_EMAIL_NONE = 'ایمیلی برای شما ثبت نشده است'
    ERR_EMAIL_VERIFIED = 'ایمیل شما تایید شده است'
    ERR_AGENCY_CONFIRMED = 'حساب حقوقی شما هم اکنون تایید شده است و امکان ثبت مجددا ندارد.'
    ERR_AGENCY_QUEUE = 'حساب حقوقی شما در حال بررسی است و امکان ثبت مجددا وجود ندارد.'
    ERR_BANK_ACCOUNT_EXIST = 'هم اکنون یک حساب بانکی با این مشخصات وجود دارد.'
    ERR_ITINERARY_PLAN_EXIST = 'برنامه سفر وجود دارد و امکان ثبت مجدد ندارد'
    ERR_BALANCE_IS_NOT_ENOUGH = 'موجودی کیف پول کمتر مقدار برداشتی می باشد'

    # Basic
    ERR_LOCATION_NOT_FOUND = 'مکان مورد نظر وجود ندارد'
    ERR_IMAGE_NOT_FOUND = 'تصویر مورد نظر وجود ندارد'

    # ***** Location *****
    ERR_LOC_COMMENT_NOT_FOUND = 'نظر یافت نشد'

    # Support
    ERR_SUP_CONTACT_FORM_DUPLICATE = 'شما یک درخواست با مشخصات مشابه ثبت نموده اید، امکان ثبت مجدد وجود ندارد'
    ERR_SUP_DOES_NOT_EXIST = 'درخواستی با مشخصات ارسالی وجود ندارد'

    # Validation
    ERR_VLD_PHONE_NUMBER = 'شماره تلفن باید 11 رقم و به صورت 09xxxxxxxxx باشد'
    ERR_VLD_USERNAME = 'نام کاربری با حروف انگلیسی باشد'
    ERR_VLD_NAME = 'نام و نام خانوادگی باید حداقل 2 حرف و با حروف فارسی باشند'
    ERR_VLD_PASSWORD = 'رمز عبور باید شامل حداقل 8 حرف و شامل 1 حرف انگلیسی بزرگ، 1 حرف انگلیسی کوچک، 1 عدد و 1 ' \
                       'کاراکتر خاص باشد.'

    # Reserve
    ERR_ORDER_NOT_FOUND = 'سفارش یافت نشد'
    ERR_ORDER_CANCEL_NOT_CONFIRM = 'سفارش تایید نشده امکان استرداد ندارد'
    ERR_RESERVE_PERSONS_INVALID = 'تعداد یا اطلاعات مسافران صحیح نیست'
    ERR_RESERVE_PRICE_INVALID = 'مبلغ قابل پرداخت صحیح نیست'
    ERR_PAYMENT_NOT_FOUND = 'مشخصات پرداخت شما پیدا نشد لطفا با تیم پشتیبانی تماس حاصل فرمایید'
    ERR_SUBSCRIBE_NOT_FOUND = 'اشتراک مورد نظر در دسترس نمیباشد'
    ERR_TOUR_NOT_FOUND = 'تور یافت نشد'

    # Sep OPG
    SEP_VERIFY_NOT_FOUND = 'تراکنش یافت نشد.'
    SEP_VERIFY_EXPIRED = 'بیش از نیم ساعت از زمان اجرای تراکنش گذشته است'
    SEP_VERIFY_DUPLICATE = 'درخواست تکراری می باشد.'
    SEP_VERIFY_TERMINAL_NOT_FOUND = 'ترمینال ارسالی در سیستم موجود نمی باشد'
    SEP_VERIFY_TERMINAL_DISABLE = 'ترمینال ارسال ی غیر فعال می باشد'
    SEP_VERIFY_IP_INVALID = 'آدرس آی پی درخواستی غیر مجاز می باشد'

    # Admin
    ERR_USER_EXIST = 'کاربر با این شماره تلفن، نام کاربری یا کد ملی وجود دارد'
    ERR_BANK_ACCOUNT_NOT_FOUND = 'حساب بانکی با این مشخصات وجود ندارد'
    ERR_USER_SETTING_NOT_FOUND = 'دریافت تنظیمات با خطا مواجه شد'

    """
        Success
    """

    # General
    OK_EDITED = 'عملیات ویرایش با موفقیت انجام گردید'
    OK_CREATED = 'عملیات ثبت با موفقیت انجام گردید'
    OK_DELETED = 'عملیات حذف با موفقیت انجام گردید'

    # Authentication
    OK_REGISTER = 'ثبت نام با موفقیت انجام گردید'
    OK_LOGIN_OTP_SENT = 'یکبار رمز با موفقیت ارسال گردید.'

    # Accounts
    OK_OTP_SENT = 'یکبار رمز با موفقیت ارسال شد.'
    OK_RESET_PASSWORD = 'رمز عبور با موفقیت تغییر کرد'
    OK_PASSENGER = 'همسفر با موفقیت ثبت شد'
    OK_PASSENGER_REMOVE = 'همسفر با موفقیت حذف گردید'
    OK_PHONE_CONFIRMED = 'تلفن همراه شما با موفقیت تایید شد'
    OK_EMAIL_CONFIRMED = 'ایمیل شما با موفقیت تایید شد.'
    OK_TRANSFER_COMPLETE = 'تراکنش با موفقیت انجام شد'

    # Support
    OK_SUP_REGISTER = 'درخواست با موفقیت ثبت گردید و بزودی توسط تیم پشتیبانی بررسی می شود.'

    # Sep OPG
    SEP_VERIFY_OK = 'عملیات با موفقیت انجام شد'


class SiteOptions:
    SITE_PUBLIC_BANNER = 'SITE_PUBLIC_BANNER'  # بنر سایت
