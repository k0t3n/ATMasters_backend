from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from src.apps.subway.models import SubwayStation
from src.apps.subway.serializers import SubwayStationDetailedSerializer, SubwayStationSerializer


class SubwayStationsListView(viewsets.ReadOnlyModelViewSet):
    queryset = SubwayStation.objects.all()
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SubwayStationDetailedSerializer

        return SubwayStationSerializer
