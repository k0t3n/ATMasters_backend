from django_filters import rest_framework as filters
from rest_framework import viewsets

from src.apps.withdrawal_point.filters import NearestItemsFilter, WithdrawalPointBanksFilter, \
    WithdrawalPointSimpleFieldsFilterSet
from src.apps.withdrawal_point.models import WithdrawalPoint
from src.apps.withdrawal_point.serializers import WithdrawalPointSerializer


class WithdrawalPointListView(viewsets.ReadOnlyModelViewSet):
    queryset = WithdrawalPoint.objects.all()
    serializer_class = WithdrawalPointSerializer
    distance_filter_field = 'coordinates'
    filterset_class = WithdrawalPointSimpleFieldsFilterSet
    filter_backends = (
        NearestItemsFilter,
        WithdrawalPointBanksFilter,
        filters.DjangoFilterBackend,
    )
