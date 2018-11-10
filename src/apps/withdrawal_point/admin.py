from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets import GooglePointFieldWidget
from suit.admin import RelatedFieldAdmin

from .models import Schedule, WithdrawalPoint


@admin.register(WithdrawalPoint)
class WithdrawalPointAdmin(RelatedFieldAdmin):

    # TODO: fails on select_related, so we use code from admin.ModelAdmin instead
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        return qs

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
    list_display = (
        'point_type', 'bank', 'address', 'cash_in',
        'cash_out', 'contactless_payments', 'mobile_payments',
        'disabled_access', 'self_collection'
    )
    search_fields = ('address', 'point_type')
    list_filter = ('point_type', 'bank', 'schedule')
    list_select_related = True
    filter_horizontal = ('schedule',)


@admin.register(Schedule)
class ScheduleAdmin(RelatedFieldAdmin):
    search_fields = ('start_day', 'is_round_the_clock', 'is_closed')
    list_display = ('start_day', 'end_day', 'start_time', 'end_time', 'is_round_the_clock', 'is_closed')
    list_filter = ('start_day', 'is_round_the_clock', 'is_closed')
    list_select_related = True
