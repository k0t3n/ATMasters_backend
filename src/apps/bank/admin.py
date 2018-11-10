from django.contrib import admin
from suit.admin import RelatedFieldAdmin

from .models import Bank


@admin.register(Bank)
class BankAdmin(RelatedFieldAdmin):
    search_fields = ('title', 'site')
    list_display = ('title', 'site')
    list_filter = ('title',)
