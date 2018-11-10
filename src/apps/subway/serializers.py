from rest_framework import serializers
from src.apps.subway.models import SubwayStation


class SubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStation
        fields = '__all__'
