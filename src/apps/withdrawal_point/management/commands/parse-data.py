import json
import os

from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from src.apps.bank.models import Bank
from src.apps.currency.models import Currency
from src.apps.withdrawal_point.models import Schedule, WithdrawalPoint


class Command(BaseCommand):
    help = 'Parse withdrawal points'

    def handle(self, *args, **options):
        data_file = os.path.join(settings.BASE_DIR, 'data/atm-data.json')
        schedules = [
            Schedule.objects.get_or_create(
                start_day=Schedule.MONDAY_CHOICE, end_day=Schedule.FRIDAY_CHOICE,
                start_time='09:00', end_time='18:00'
            )[0],
            Schedule.objects.get_or_create(
                start_day=Schedule.SATURDAY_CHOICE, end_day=Schedule.SUNDAY_CHOICE,
                start_time='10:00', end_time='16:00'
            )[0],
        ]
        with open(data_file) as file:
            data = json.load(file)

        for point in data:
            bank_title = point['properties']['name'].split(',')[0]
            bank_url = point['properties']['CompanyMetaData'].get('url')
            bank = Bank.objects.get_or_create(
                title=bank_title,
                defaults={
                    'site': bank_url
                }
            )[0]

            address = point['properties']['CompanyMetaData']['address']
            longitude = point['geometry']['coordinates'][0]
            latitude = point['geometry']['coordinates'][1]

            withdrawal_point = WithdrawalPoint.objects.get_or_create(
                coordinates=Point(longitude, latitude),
                defaults={
                    'bank': bank,
                    'address': address,
                    'cash_in': True,
                    'cash_out': True,
                }
            )[0]

            for schedule in schedules:
                withdrawal_point.schedule.add(schedule)

            withdrawal_point.currencies.add(Currency.objects.get(title='Рубль'))

            withdrawal_point.save()
