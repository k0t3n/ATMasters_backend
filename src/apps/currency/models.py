from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('название')
    )
    iso_name = models.CharField(
        max_length=3,
        unique=True,
        verbose_name=_('ISO 4217')
    )

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'

    def __str__(self):
        return self.title
