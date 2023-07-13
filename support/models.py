from django.db import models
from django.core.exceptions import ValidationError


class Support(models.Model):
    creator = models.CharField(max_length=45, null=True, blank=False)  # نام ثبت کننده
    date_time = models.DateTimeField(null=True, auto_now_add=True)  # تاریخ و ساعت ثبت کننده
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)  # رایانامه ثبت کننده
    phone_number = models.CharField(max_length=15, null=True)  # شماره تلفن ثبت کننده
    ip = models.CharField(max_length=15, null=True)  # IP ثبت کننده
    message = models.TextField(null=True)  # متن پیام
    subjects = models.ManyToManyField('Subject', blank=True)
    viewer = models.ForeignKey('accounts.User', models.CASCADE, 'scf_viewer', to_field='id', null=True, blank=True)  # پشتیبان
    viewed_date = models.DateTimeField(null=True, blank=True)  # ساعت مشاهده پشتیبان

    def __str__(self):
        return f'{self.creator} - {self.email}'


class Subject(models.Model):
    parent = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='childs', null=True, blank=True)
    is_child = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
