from rest_framework import viewsets

from src.apps.withdrawal_point.filters import NearestItemsFilter, WithdrawalPointBanksFilter
from src.apps.withdrawal_point.models import WithdrawalPoint
from src.apps.withdrawal_point.serializers import WithdrawalPointSerializer


class WithdrawalPointListView(viewsets.ReadOnlyModelViewSet):
    queryset = WithdrawalPoint.objects.all()
    serializer_class = WithdrawalPointSerializer
    distance_filter_field = 'coordinates'
    filter_backends = (
        NearestItemsFilter,
        WithdrawalPointBanksFilter,
    )
