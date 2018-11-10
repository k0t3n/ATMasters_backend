from rest_framework import serializers
from src.apps.withdrawal_point.models import WithdrawalPoint, Schedule
from src.apps.currency.serializers import CurrencySerializer
from src.apps.bank.serializers import BankSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class WithdrawalPointSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True)
    currencies = CurrencySerializer(many=True)
    bank = BankSerializer()

    class Meta:
        model = WithdrawalPoint
        fields = (
            'id', 'point_type', 'bank', 'coords', 'schedule',
            'currencies', 'is_nfc', 'is_disabled_access', 'is_working_now'
        )
