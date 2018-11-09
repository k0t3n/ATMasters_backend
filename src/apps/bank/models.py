from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bank(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
    )

    class Meta:
        verbose_name = _('banks')
        verbose_name_plural = _('bank')

    def __str__(self):
        return self.title
