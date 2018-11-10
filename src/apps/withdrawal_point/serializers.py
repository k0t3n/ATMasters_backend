from rest_framework import serializers

from src.apps.withdrawal_point.models import WithdrawalPoint, Schedule
from src.apps.currency.serializers import CurrencySerializer
from src.apps.bank.serializers import BankSerializer

from src.apps.subway.serializers import SubwayStationSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class WithdrawalPointSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True)
    currencies = CurrencySerializer(many=True)
    closest_subway = SubwayStationSerializer()
    distance = serializers.CharField(read_only=True)
    bank = BankSerializer()

    class Meta:
        model = WithdrawalPoint
        fields = (
            'id', 'point_type', 'bank', 'closest_subway', 'coords', 'address', 'schedule', 'currencies',
            'cash_in', 'cash_out', 'contactless_payments', 'mobile_payments', 'disabled_access',
            'self_collection', 'is_working_now', 'distance'
        )
