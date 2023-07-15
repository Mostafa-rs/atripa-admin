"""
مجوزهای اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.pk == request.user.pk
        return obj == request.user

