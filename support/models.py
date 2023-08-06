from django.db import models
from django.core.exceptions import ValidationError
import jdatetime


class Support(models.Model):
    creator = models.ForeignKey('accounts.User', on_delete=models.RESTRICT, null=True, blank=False)
    date_time = models.DateTimeField(null=True, auto_now_add=True)  # تاریخ و ساعت ثبت کننده
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)  # رایانامه ثبت کننده
    phone_number = models.CharField(max_length=15, null=True)  # شماره تلفن ثبت کننده
    ip = models.CharField(max_length=15, null=True)  # IP ثبت کننده
    message = models.TextField(null=True)  # متن پیام
    subjects = models.ManyToManyField('Subject', blank=True)
    viewer = models.ForeignKey('accounts.User', models.CASCADE, 'scf_viewer', to_field='id', null=True, blank=True)  # پشتیبان
    viewed_date = models.DateTimeField(null=True, blank=True)  # ساعت مشاهده پشتیبان
    closed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.creator} - {self.email}'

    def get_subjects(self):
        subjects = self.subjects.all()
        result = ''
        for i in subjects:
            result += i.name + ' - '
        return result[:-3]

    # def created(self):
    #     return f'{self.date_time.date()} {self.date_time.hour}:{self.date_time.minute}:{self.date_time.second}'

    @property
    def date_time_persian(self):
        result = str(jdatetime.datetime.fromgregorian(datetime=self.date_time))
        return result[:-12]

    @property
    def modified_persian(self):
        result = str(jdatetime.datetime.fromgregorian(datetime=self.modified))
        return result[:-12]


class Subject(models.Model):
    parent = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='childs', null=True, blank=True)
    is_child = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Chat(models.Model):
    support = models.ForeignKey('Support', on_delete=models.RESTRICT)
    sender = models.ForeignKey('accounts.User', on_delete=models.RESTRICT, related_name='sent_messages')
    receiver = models.ForeignKey('accounts.User', on_delete=models.RESTRICT, related_name='received_messages',
                                 null=True, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.support.creator.full_name}'

    def sent_at_persian(self):
        result = str(jdatetime.datetime.fromgregorian(datetime=self.sent_at))
        res = result.split(' ')
        return res[0] + ' | ' + res[1][:-5]
