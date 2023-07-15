"""
سریالایزر دیتا اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', )



