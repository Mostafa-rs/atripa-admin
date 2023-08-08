from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'phone_number', 'is_staff', 'is_superuser')
    list_filter = ('is_staff',)
    fieldsets = (
        (
            None,
            {'fields': ('email', 'username', 'phone_number', 'home_number', 'emergency_number', 'first_name',
                        'last_name', 'english_first_name', 'english_last_name', 'type', 'email_confirmed',
                        'phone_confirmed', 'last_login_ip', 'creator', 'gender', 'representative',
                        'representative_code', 'education', 'major', 'country', 'province', 'city',
                        'place_of_birth', 'birthdate', 'father_name', 'national_code',
                        'postal_code', 'passport_no', 'passport_expiry_date', 'passport_issue_date',
                        'address', 'password')}
        ),
        (
            'permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login',
                        'date_joined')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {'fields': ('username', 'email', 'first_name', 'last_name', 'english_first_name', 'english_last_name',
                        'home_number', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('phone_number', 'email')
    ordering = ('first_name',)
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form


admin.site.register(models.Agency)
admin.site.register(models.UserType)
admin.site.register(models.UserBankAccount)
admin.site.register(models.UserConfirmation)
admin.site.register(models.UserFavorites)
admin.site.register(models.UserItineraryPlan)
admin.site.register(models.UserPassenger)
admin.site.register(models.UserReward)
admin.site.register(models.UserRewardUsage)
admin.site.register(models.UserPoint)
admin.site.register(models.UserTransaction)
admin.site.register(models.UserSupportRequest)
admin.site.register(models.UserSupportChat)
admin.site.register(models.UserSetting)
admin.site.register(models.UserSubscribe)