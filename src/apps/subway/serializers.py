from rest_framework import serializers

from src.apps.subway.models import SubwayStation
from src.apps.withdrawal_point.serializers import WithdrawalPointSerializer


class SubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStation
        fields = ('id', 'title', 'coords', 'branch_color',)


class SubwayStationDetailedSerializer(serializers.ModelSerializer):
    nearest_withdrawal_points = WithdrawalPointSerializer(many=True)

    class Meta:
        model = SubwayStation
        fields = ('id', 'title', 'coords', 'branch_color', 'nearest_withdrawal_points')
