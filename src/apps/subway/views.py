from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from src.apps.subway.models import SubwayStation
from src.apps.subway.serializers import SubwayStationSerializer


class SubwayStationsListView(viewsets.ReadOnlyModelViewSet):
    queryset = SubwayStation.objects.all()
    serializer_class = SubwayStationSerializer
    pagination_class = PageNumberPagination
