from django.db import models
from django.utils.translation import ugettext_lazy as _


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
