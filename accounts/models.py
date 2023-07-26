"""
دیتابیس اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_jalali.db import models as jmodels
from .managers import UserManager
from .utils import path_and_rename


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    en_full_name = models.CharField(max_length=255)
    subscribe = models.ForeignKey('basic.Subscribe', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    b_day = models.CharField(null=True, blank=True, max_length=200)
    static_number = models.CharField(max_length=40, null=True, blank=True)
    mobile_number = models.CharField(max_length=30, null=True, blank=True)
    passport_no = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    fathers_name = models.CharField(max_length=200, null=True, blank=True)
    national_id = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    passport_exp = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name', 'en_full_name')

    def __str__(self):
        return f'{self.email} - {self.en_full_name}'

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True

    @property
    def is_staff(self):
        return self.is_admin
