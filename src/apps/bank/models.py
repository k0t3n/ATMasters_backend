from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bank(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('название'),
    )

    class Meta:
        verbose_name = _('банки')
        verbose_name_plural = _('банк')

    def __str__(self):
        return self.title
