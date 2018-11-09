from django.db import models
from django.db.models import Case, When, F
from rest_framework import viewsets

from src.apps.withdrawal_point.filters import NearestItemsFilter, WithdrawalPointBankFilter
from src.apps.withdrawal_point.models import WithdrawalPoint
from src.apps.withdrawal_point.serializers import WithdrawalPointSerializer


class CustomQuerySet(models.QuerySet):
    def annotate_with_custom_field(self):
        return self.annotate(
            custom_field=Case(
                When(foo__isnull=False,
                     then=F('foo__uuid')),
                When(bar__isnull=False,
                     then=F('bar__uuid')),
                default=None,
            ),
        )


class WithdrawalPointListView(viewsets.ReadOnlyModelViewSet):
    queryset = WithdrawalPoint.objects.all()
    serializer_class = WithdrawalPointSerializer
    distance_filter_field = 'coordinates'
    filter_backends = (
        NearestItemsFilter,
        WithdrawalPointBankFilter,
    )
