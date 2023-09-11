from rest_framework import permissions


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.is_staff)


class IsSuperUserOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_superuser or request.user == obj)

