from django.contrib import admin
from . import models


class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator')


admin.site.register(models.Support, SupportAdmin)
admin.site.register(models.Subject)
