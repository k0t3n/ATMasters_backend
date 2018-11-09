from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets import GooglePointFieldWidget

from .models import Schedule, WithdrawalPoint


class WithdrawalPointAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


# TODO: admin
admin.site.register(Schedule)
admin.site.register(WithdrawalPoint, WithdrawalPointAdmin)
