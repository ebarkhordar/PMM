# Register your models here.
from installations.models import Device

from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin


class DeviceAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass


admin.site.register(Device, DeviceAdmin)
