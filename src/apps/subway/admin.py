from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets import GooglePointFieldWidget
from suit.admin import RelatedFieldAdmin

from .models import SubwayStation


@admin.register(SubwayStation)
class SubwayStationAdmin(RelatedFieldAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
    search_fields = ('title', 'branch_color')
    list_display = ('title', 'branch_color')
    list_filter = ('branch_color',)
