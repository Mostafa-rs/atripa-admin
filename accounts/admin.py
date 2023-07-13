from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'mobile_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (
            None,
            {'fields': ('email', 'mobile_number', 'full_name', 'en_full_name', 'b_day', 'static_number',
                        'passport_no', 'fathers_name', 'national_id', 'postal_code', 'passport_exp', 'address', 'image',
                        'password')}
        ),
        (
            'permissions',
            {'fields': ('is_active', 'is_admin', 'last_login')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {'fields': ('static_number', 'email', 'full_name', 'en_full_name', 'password1', 'password2', 'is_active',
                        'is_admin')}
        ),
    )
    search_fields = ('mobile_number', 'email')
    ordering = ('full_name',)
    readonly_fields = ('last_login',)
    filter_horizontal = ()


admin.site.unregister(Group)