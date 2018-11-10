from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance
from django.utils.translation import ugettext_lazy as _

from src.apps.withdrawal_point.models import WithdrawalPoint


class SubwayStation(models.Model):
    RED_COLOR_CHOICE = 'red'
    BLUE_COLOR_CHOICE = 'blue'
    GREEN_COLOR_CHOICE = 'green'
    ORANGE_COLOR_CHOICE = 'orange'
    PURPLE_COLOR_CHOICE = 'purple'

    BRANCH_COLOR_CHOICES = (
        (RED_COLOR_CHOICE, 'красная'),
        (BLUE_COLOR_CHOICE, 'синяя'),
        (GREEN_COLOR_CHOICE, 'зеленая'),
        (ORANGE_COLOR_CHOICE, 'оранжевая'),
        (PURPLE_COLOR_CHOICE, 'фиолетовая'),
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_('название'),
    )

    coordinates = models.PointField(
        verbose_name=_('координаты'),
        null=True
    )

    branch_color = models.CharField(
        max_length=16,
        choices=BRANCH_COLOR_CHOICES,
        verbose_name=_('ветка')
    )

    class Meta:
        verbose_name = _('станция')
        verbose_name_plural = _('станции')

    def __str__(self):
        return self.title

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y

    @property
    def coords(self):
        return {'latitude': self.latitude, 'longitude': self.longitude}

    @property
    def nearest_withdrawal_points(self):
        radius = 1000  # meters
        return WithdrawalPoint.objects.filter(
            coordinates__distance_lt=(self.coordinates, Distance(m=radius))
        )
