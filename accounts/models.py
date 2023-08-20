"""
    Account Database Models
    Author: Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/07
"""
import jdatetime
# System
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Gender:
        NOT_SPECIFIC = 0
        MALE = 1
        FEMALE = 2

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=45, unique=True, null=False, blank=False)
    type = models.ForeignKey("accounts.UserType", models.RESTRICT, "au_type", null=True, to_field="id", blank=True)
    email_confirmed = models.BooleanField(default=False)
    phone_confirmed = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    last_login_ip = models.CharField(max_length=15, null=True, blank=True)
    date_joined = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    creator = models.ForeignKey("accounts.User", models.RESTRICT, "au_creator", null=True, to_field="id", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=45, null=False, blank=True)
    last_name = models.CharField(max_length=45, null=False, blank=True)
    english_first_name = models.CharField(max_length=45, default="", blank=True)
    english_last_name = models.CharField(max_length=45, default="", blank=True)
    father_name = models.CharField(max_length=45, default="", blank=True)
    national_code = models.CharField(max_length=10, default="0000000000")
    passport_no = models.CharField(max_length=8, default="00000000")
    passport_issue_date = models.DateField(null=True, blank=True)
    passport_expiry_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(default=Gender.NOT_SPECIFIC)
    birthdate = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=45, null=True, blank=True)
    representative = models.ForeignKey("accounts.User", models.CASCADE, "au_representative", null=True, to_field="id",
                                       blank=True)
    representative_code = models.CharField(max_length=8, null=True, blank=True)
    education = models.CharField(max_length=45, null=True, blank=True)
    major = models.CharField(max_length=45, null=True, blank=True)
    # avatar = models.ImageField(upload_to=RenamePathFile('account/profile'), null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, default="", blank=True)
    home_number = models.CharField(max_length=15, null=True, blank=True)
    emergency_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.ForeignKey("basic.Country", models.RESTRICT, "au_country", null=True, to_field="id", blank=True)
    province = models.ForeignKey("basic.Province", models.RESTRICT, "au_province", null=True, to_field="id", blank=True)
    city = models.ForeignKey("basic.City", models.RESTRICT, "au_city", null=True, to_field="id", blank=True)
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    @property
    def get_birthdate_persian(self):
        if self.birthdate:
            result = str(jdatetime.date.fromgregorian(date=self.birthdate))
            return result
        return ' '
    @property
    def get_passport_expiry_date_persian(self):
        if self.passport_expiry_date:
            result = str(jdatetime.date.fromgregorian(date=self.passport_expiry_date))
            return result
        return ' '

    @property
    def get_full_name_persian(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_full_name_english(self):
        return f'{self.english_first_name} {self.english_last_name}'

    @property
    def income(self):
        _deposit = [
            UserTransaction.Type.DEPOSIT_ONLINE,
            UserTransaction.Type.DEPOSIT_RECEIPT,
            UserTransaction.Type.DEPOSIT_REWARD,
            UserTransaction.Type.DEPOSIT_CRYPTO,
            UserTransaction.Type.DEPOSIT_TRANSFER
        ]
        _income = UserTransaction.objects.filter(
            user=self,
            type__in=_deposit,
            confirm=True,
            status=UserTransaction.Status.PAID
        ).aggregate(models.Sum("amount"))["amount__sum"]

        if _income is None:
            _income = 0

        return _income

    @property
    def spend(self):
        _withdraw = [
            UserTransaction.Type.WITHDRAW_ONLINE,
            UserTransaction.Type.WITHDRAW_REFUND,
            UserTransaction.Type.WITHDRAW_BUY,
            UserTransaction.Type.WITHDRAW_CRYPTO,
            UserTransaction.Type.WITHDRAW_TRANSFER
        ]
        _spend = UserTransaction.objects.filter(
            user=self,
            type__in=_withdraw,
            confirm=True,
            status=UserTransaction.Status.WITHDRAW
        ).aggregate(models.Sum("amount"))["amount__sum"]

        if _spend is None:
            _spend = 0

        return _spend

    @property
    def balance(self):
        return self.income - self.spend


class Agency(models.Model):
    """
        Agency & Legal information table
        """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("accounts.User", models.CASCADE, "aa_user", to_field="id", null=True)
    logo = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    day_of_establishment = models.DateField(null=True)
    national_id = models.CharField(max_length=10, null=True)
    economic_code = models.CharField(max_length=16, null=True)
    ceo = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    country = models.ForeignKey("basic.Country", models.CASCADE, "aa_country", to_field="id", null=True)
    province = models.ForeignKey("basic.Province", models.CASCADE, "aa_province", to_field="id", null=True)
    city = models.ForeignKey("basic.City", models.CASCADE, "aa_city", to_field="id", null=True)
    address = models.TextField(null=True)
    postal_code = models.CharField(max_length=10, null=True)
    introduce_letter = models.TextField(null=True)
    confirmed = models.BooleanField(default=False)
    date_registered = models.DateTimeField(null=True)


class UserType(models.Model):
    """
        types of user table
        """

    class Meta:
        db_table = "account_user_type"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False, unique=True)
    modifier = models.ForeignKey("accounts.User", models.RESTRICT, related_name="ut_modifier", null=True, to_field="id")
    modified_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)


class UserConfirmation(models.Model):
    """
        confirms code for user authorization table
        """

    class Meta:
        db_table = "account_user_confirmation"

    class Type:
        LOGIN_OTP = 1
        PHONE_CONFIRM = 2
        EMAIL_CONFIRM = 3
        LEGAL_CONFIRM = 4
        WITHDRAW_CONFIRM = 5

    user = models.ForeignKey("accounts.User", models.CASCADE, "auc_user", to_field="id", null=True)
    code = models.CharField(max_length=6, null=True)
    type = models.IntegerField(default=Type.LOGIN_OTP)
    request_date = models.DateTimeField(null=True)
    request_expire = models.DateTimeField(null=True)
    used_date = models.DateTimeField(null=True)
    reference = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)


class UserPassenger(models.Model):
    """
        user's passengers table
    """

    class Meta:
        db_table = "account_user_passenger"

    user = models.ForeignKey("accounts.User", models.CASCADE, "aup_user", null=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    english_first_name = models.CharField(max_length=45, null=True)
    english_last_name = models.CharField(max_length=45, null=True)
    national_code = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    passport_no = models.CharField(max_length=8, null=True)
    passport_issue_date = models.DateField(null=True)
    passport_expiry_date = models.DateField(null=True)
    gender = models.IntegerField(default=User.Gender.NOT_SPECIFIC)
    birthdate = models.DateField(null=True)
    nationality = models.ForeignKey('basic.Country', models.CASCADE, 'aup_country', null=True)


class UserBankAccount(models.Model):
    """
        user's bank accounts information table
    """

    class Meta:
        db_table = "account_user_bank_account"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("accounts.User", models.CASCADE, "buba_user", to_field="id", null=True)
    bank = models.ForeignKey("basic.Bank", models.CASCADE, "buba_bank", to_field="id", null=True)
    card_number = models.CharField(max_length=16, null=True)
    account_number = models.CharField(max_length=45, null=True)
    sheba_number = models.CharField(max_length=24, null=True)
    confirmed = models.BooleanField(default=False)
    date_registered = models.DateTimeField(null=True)


class UserItineraryPlan(models.Model):
    """
        جدول اطلاعات برنامه سفر کاربر
    """
    class Meta:
        db_table = "account_user_itinerary_plan"
        unique_together = ("user", "plan")

    user = models.ForeignKey("accounts.User", models.CASCADE, "auip_user", to_field="id", null=True)
    plan = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(null=True)


class UserPoint(models.Model):
    class Meta:
        db_table = "account_user_point"

    user = models.ForeignKey("accounts.User", models.CASCADE, "aupo_user", to_field="id", null=True)
    date = models.DateTimeField(null=True)
    point = models.IntegerField(default=0)
    date_validate = models.DateTimeField(null=True)
    description = models.TextField(null=True)


class UserReward(models.Model):
    class Meta:
        db_table = "account_user_reward"

    user = models.ForeignKey("accounts.User", models.CASCADE, 'aur_user', to_field='id', null=True)
    reward = models.ForeignKey("club.Reward", models.CASCADE, 'aur_reward', to_field='id', null=True)
    code = models.CharField(max_length=12, null=True)
    date_validate = models.DateTimeField(null=True)
    usage_validate = models.IntegerField(default=1)
    date = models.DateTimeField(null=True)
    point = models.IntegerField(default=0)


class UserRewardUsage(models.Model):
    class Meta:
        db_table = "account_user_reward_usage"

    reward = models.ForeignKey("accounts.UserReward", models.CASCADE, 'auru_reward', to_field="id", null=True)
    date = models.DateTimeField(null=True)
    ip = models.CharField(max_length=15, null=True)


class UserTransaction(models.Model):
    """
        user's wallet transactions information table
        """

    class Meta:
        db_table = "account_user_transaction"

    class Type:
        DEPOSIT_ONLINE = 0
        DEPOSIT_RECEIPT = 1
        DEPOSIT_REWARD = 2
        DEPOSIT_CRYPTO = 3
        DEPOSIT_TRANSFER = 4
        WITHDRAW_ONLINE = 10
        WITHDRAW_REFUND = 11
        WITHDRAW_BUY = 12
        WITHDRAW_CRYPTO = 13
        WITHDRAW_TRANSFER = 14

    class Status:
        PENDING_PAYMENT = 0
        PAID = 1
        CANCELED = 2
        REFUNDING = 3
        REFUND = 4
        PENDING_WITHDRAW = 5
        WITHDRAW = 6

    user = models.ForeignKey('accounts.User', models.CASCADE, 'aut_user', to_field='id', null=True)
    date = models.DateTimeField(null=True)
    amount = models.PositiveIntegerField(default=0)
    reference_id = models.CharField(max_length=45, null=True)
    type = models.IntegerField(default=Type.DEPOSIT_ONLINE, help_text='0-4 deposit   10-14 withdraw')
    status = models.IntegerField(default=Status.PENDING_PAYMENT, help_text='0 pending 1 paid 2 canceled 3 refunding '
                                                                           '4 refund 5 pending withdraw 6 withdraw')
    wallet_balance = models.IntegerField(default=0)
    payment_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    redirect_code = models.CharField(max_length=45, null=True)
    authority = models.CharField(max_length=45, null=True)
    confirm = models.BooleanField(default=False)
    card_hash = models.CharField(max_length=45, null=True)
    card_number = models.CharField(max_length=16, null=True)

    @property
    def get_type(self):
        match self.type:
            case UserTransaction.Type.DEPOSIT_ONLINE:
                return "افزایش اعتبار - پرداخت آنلاین"
            case UserTransaction.Type.DEPOSIT_RECEIPT:
                return "افزایش اعتبار - پرداخت با فیش بانکی"
            case UserTransaction.Type.DEPOSIT_REWARD:
                return "افزایش اعتبار - دریافت جایزه"
            case UserTransaction.Type.DEPOSIT_CRYPTO:
                return "افزایش اعتبار - پرداخت با رمزارز"
            case UserTransaction.Type.DEPOSIT_TRANSFER:
                return "افزایش اعتبار - انتقال از کاربران"
            case UserTransaction.Type.WITHDRAW_ONLINE:
                return "کاهش اعتبار - برداشت آنلاین"
            case UserTransaction.Type.WITHDRAW_REFUND:
                return "کاهش اعتبار - استرداد وجه"
            case UserTransaction.Type.WITHDRAW_BUY:
                return "کاهش اعتبار - خرید خدمات"
            case UserTransaction.Type.WITHDRAW_CRYPTO:
                return "کاهش اعتبار - برداشت رمزارز"
            case UserTransaction.Type.WITHDRAW_TRANSFER:
                return "کاهش اعتبار - انتقال به کاربران"
            case _:
                return "نا مشخص"

    @property
    def get_status(self):
        match self.status:
            case UserTransaction.Status.PENDING_PAYMENT:
                return "در انتظار پرداخت"
            case UserTransaction.Status.PAID:
                return "پرداخت شده"
            case UserTransaction.Status.CANCELED:
                return "لغو شده"
            case UserTransaction.Status.REFUNDING:
                return "در حال استرداد"
            case UserTransaction.Status.REFUND:
                return "مسترد"
            case UserTransaction.Status.PENDING_WITHDRAW:
                return "در انتظار برداشت"
            case UserTransaction.Status.WITHDRAW:
                return "برداشت شده"
            case _:
                return "نامشخص"

    def get_type_sign(self):
        if self.type in [0, 1, 2, 3, 4]:
            return True
        elif self.type in [10, 11, 12, 13, 14]:
            return False
        else:
            return None


class UserSupportRequest(models.Model):
    """
        user's support requests information table
        """

    class Meta:
        db_table = 'account_user_support_request'

    class Status:
        USER_REPLY = 0
        SUPPORT_REPLY = 1
        CLOSED_BY_USER = 2
        CLOSED_BY_SUPPORT = 3
        COMPLAIN = 4

    user = models.ForeignKey('accounts.User', models.CASCADE, 'ausr_user', to_field='id', null=True)
    type = models.ForeignKey('basic.SupportType', models.CASCADE, 'ausr_type', to_field='id', null=True)
    register_date = models.DateTimeField(null=True)
    last_modified_date = models.DateTimeField(null=True)
    title = models.TextField(max_length=30, null=True)
    status = models.IntegerField(default=Status.USER_REPLY)
    supporter = models.ForeignKey('accounts.User', models.CASCADE, 'ausr_supporter', to_field='id', null=True)

    @property
    def get_status(self):
        match self.status:
            case UserSupportRequest.Status.USER_REPLY:
                return "در انتظار پاسخ پشتیبان"
            case UserSupportRequest.Status.SUPPORT_REPLY:
                return "پاسخ داده شده"
            case UserSupportRequest.Status.CLOSED_BY_USER:
                return "بسته شده توسط کاربر"
            case UserSupportRequest.Status.CLOSED_BY_SUPPORT:
                return "بسته شده"
            case UserSupportRequest.Status.COMPLAIN:
                return "بررسی توسط ناظر"
            case _:
                return "نامشخص"


class UserSupportChat(models.Model):
    """
        user's support request's chats table
        """

    class Meta:
        db_table = 'account_user_support_chat'

    class Type:
        USER = 0
        SUPPORTER = 1

    request = models.ForeignKey('accounts.UserSupportRequest', models.CASCADE, 'ausc_support', to_field='id', null=True)
    user = models.ForeignKey("accounts.User", models.CASCADE, 'ausc_user', to_field="id", null=True)
    type = models.IntegerField(default=Type.USER)
    date = models.DateTimeField(null=True)
    attach = models.TextField(null=True)
    text = models.TextField(null=True)


class UserFavorites(models.Model):
    """
        user's itinerary favorites table
        """

    class Meta:
        db_table = "account_user_favorites"

    user = models.ForeignKey("accounts.User", models.CASCADE, "auf_user", to_field="id", null=True)
    religious = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    nature = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    adventure = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    historical = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    art_cultural = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    shopping = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    energy_class = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    price_class = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    sleep_class = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    accommodation = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])


class UserSetting(models.Model):
    """
        user's settings table
        """

    class Meta:
        db_table = "account_user_setting"

    user = models.ForeignKey("accounts.User", models.CASCADE, "aus_user", to_field="id", null=True)
    background = models.IntegerField(default=0)
    theme = models.CharField(max_length=10, default="light", null=True)
    two_step_verification = models.BooleanField(default=False)
    login_sms = models.BooleanField(default=True)
    login_notif = models.BooleanField(default=False)
    login_email = models.BooleanField(default=False)
    withdraw_sms = models.BooleanField(default=True)
    withdraw_notif = models.BooleanField(default=False)
    withdraw_email = models.BooleanField(default=False)
    deposit_sms = models.BooleanField(default=True)
    deposit_notif = models.BooleanField(default=False)
    deposit_email = models.BooleanField(default=True)
    news_sms = models.BooleanField(default=True)
    news_notif = models.BooleanField(default=False)
    news_email = models.BooleanField(default=False)
    rss_sms = models.BooleanField(default=True)
    rss_notif = models.BooleanField(default=False)
    rss_email = models.BooleanField(default=False)
    reserve_sms = models.BooleanField(default=True)
    reserve_notif = models.BooleanField(default=False)
    reserve_email = models.BooleanField(default=False)
    reserve_change_sms = models.BooleanField(default=False)
    reserve_change_notif = models.BooleanField(default=False)
    reserve_change_email = models.BooleanField(default=False)


class UserSubscribe(models.Model):
    """
        User subscribe information table
        """

    class Meta:
        db_table = "account_user_subscribe"

    user = models.ForeignKey("accounts.User", models.CASCADE, "ausu_user", to_field="id", null=True)
    subscribe = models.ForeignKey("basic.Subscribe", models.CASCADE, "ausu_subscribe", to_field="id", null=True)
    # order = models.ForeignKey("reserve.Order", models.CASCADE, "ausu_order", to_field="id", null=True)
    expiry_date = models.DateField(null=True)


