"""
    Support models
    Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/26
"""

# System
from django.db import models


class ContactForm(models.Model):
    creator = models.CharField(max_length=45, null=True, blank=False)  # نام ثبت کننده
    date_time = models.DateTimeField(null=True)  # تاریخ و ساعت ثبت کننده
    email = models.EmailField(null=True)  # رایانامه ثبت کننده
    phone_number = models.CharField(max_length=15, null=True)  # شماره تلفن ثبت کننده
    ip = models.CharField(max_length=15, null=True)  # IP ثبت کننده
    message = models.TextField(null=True)  # متن پیام
    viewer = models.ForeignKey('accounts.User', models.CASCADE, 'scf_viewer', to_field='id', null=True)  # پشتیبان
    viewed_date = models.DateTimeField(null=True)  # ساعت مشاهده پشتیبان
