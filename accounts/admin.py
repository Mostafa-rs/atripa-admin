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
    list_display = ('email', 'mobile_number', 'is_admin', 'is_superuser')
    list_filter = ('is_admin',)
    fieldsets = (
        (
            None,
            {'fields': ('email', 'mobile_number', 'full_name', 'en_full_name', 'subscribe', 'b_day', 'static_number',
                        'passport_no', 'fathers_name', 'national_id', 'postal_code', 'passport_exp', 'address', 'image',
                        'password')}
        ),
        (
            'permissions',
            {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions', 'last_login')}
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
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form

