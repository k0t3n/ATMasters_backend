from django.contrib import admin
from suit.admin import RelatedFieldAdmin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(RelatedFieldAdmin):
    search_fields = ('title', 'iso_name')
    list_display = ('title', 'iso_name')
    list_filter = ('title', 'iso_name')
    list_select_related = True
