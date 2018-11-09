from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Schedule(models.Model):
    MONDAY_CHOICE = 'mon'
    TUESDAY_CHOICE = 'tue'
    WEDNESDAY_CHOICE = 'wed'
    THURSDAY_CHOICE = 'thu'
    FRIDAY_CHOICE = 'fri'
    SATURDAY_CHOICE = 'sat'
    SUNDAY_CHOICE = 'sun'

    WEEKDAY_CHOICES = (
        (MONDAY_CHOICE, _('понедельник')),
        (TUESDAY_CHOICE, _('вторник')),
        (WEDNESDAY_CHOICE, _('среда')),
        (THURSDAY_CHOICE, _('четверг')),
        (FRIDAY_CHOICE, _('пятница')),
        (SATURDAY_CHOICE, _('суббота')),
        (SUNDAY_CHOICE, _('воскресенье')),
    )

    start_day = models.CharField(
        max_length=3,
        choices=WEEKDAY_CHOICES,
        verbose_name=_('день начала')
    )
    end_day = models.CharField(
        max_length=3,
        choices=WEEKDAY_CHOICES,
        verbose_name=_('день окончания')
    )
    start_time = models.TimeField(
        verbose_name=_('время начала'),
        null=True, blank=True
    )
    end_time = models.TimeField(
        verbose_name=_('время окончания'),
        null=True, blank=True
    )
    is_round_the_clock = models.BooleanField(
        default=False,
        verbose_name=_('круглосуточно?')
    )

    is_closed = models.BooleanField(
        default=False,
        verbose_name=_('закрыто?')
    )

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')

    def __str__(self):
        start_day = self.get_start_day_display()
        end_day = self.get_end_day_display()

        if self.is_round_the_clock:
            return 'Круглосуточно с {} по {}'.format(start_day, end_day)
        elif self.is_closed:
            return 'Закрыто с {} по {}'.format(start_day, end_day)
        else:
            return 'С {} {} по {} {}'.format(start_day, self.start_time, end_day, self.end_time)


class WithdrawalPoint(models.Model):
    ATM_POINT_TYPE = 0
    SHOP_POINT_TYPE = 1
    BANK_POINT_TYPE = 2
    TERMINAL_POINT_TYPE = 3

    POINT_TYPE_CHOICES = (
        (ATM_POINT_TYPE, 'банкомат'),
        (SHOP_POINT_TYPE, 'магазин'),
        (BANK_POINT_TYPE, 'банк'),
        (TERMINAL_POINT_TYPE, 'терминал'),
    )

    point_type = models.CharField(
        choices=POINT_TYPE_CHOICES,
        max_length=4,
        verbose_name=_('тип точки')
    )
    bank = models.ForeignKey(
        'bank.Bank',
        on_delete=models.CASCADE,
        verbose_name=_('банк'),
        null=True, blank=True
    )
    coordinates = models.PointField(
        verbose_name=_('координаты')
    )
    schedule = models.ManyToManyField(
        'Schedule',
        verbose_name=_('расписание')
    )
    currencies = models.ManyToManyField(
        'currency.Currency',
        verbose_name=_('валюты')
    )
    is_nfc = models.NullBooleanField(
        verbose_name=_('NFC?'),
        default=None,
        null=True, blank=True,
    )
    is_disabled_access = models.NullBooleanField(
        _('доступно для инвалидов?'),
        default=None,
        null=True, blank=True
    )

    class Meta:
        verbose_name = _('Точка выдачи наличных')
        verbose_name_plural = _('Точки выдачи наличных')

    def __str__(self):
        string = self.get_point_type_display().capitalize()

        if self.bank:
            string += ', {}'.format(self.bank)

        return string

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y

    @property
    def coords(self):
        return {'latitude': self.latitude, 'longitude': self.longitude}
