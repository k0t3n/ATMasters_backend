from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bank(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('название'),
    )

    icon = models.ImageField(
        verbose_name=_('иконка'),
        null=True, blank=True
    )

    site = models.URLField(
        verbose_name=_('сайт'),
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('банки')
        verbose_name_plural = _('банк')

    def __str__(self):
        return self.title
