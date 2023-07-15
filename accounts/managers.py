"""
رابط دیتابیس اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, full_name=None, en_full_name=None, b_day=None, static_number=None,
                    mobile_number=None, passport_no=None, address=None, fathers_name=None, national_id=None,
                    postal_code=None, passport_exp=None):
        if not email:
            raise ValueError('User must have Email')

        user = self.model(email=self.normalize_email(email), full_name=full_name, en_full_name=en_full_name,
                          b_day=b_day, static_number=static_number, mobile_number=mobile_number, passport_no=passport_no,
                          address=address, fathers_name=fathers_name, national_id=national_id, postal_code=postal_code,
                          passport_exp=passport_exp)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name=None, en_full_name=None, b_day=None, static_number=None,
                         mobile_number=None, passport_no=None, address=None, fathers_name=None, national_id=None,
                         postal_code=None, passport_exp=None):
        user = self.create_user(email=email, full_name=full_name, en_full_name=en_full_name, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
