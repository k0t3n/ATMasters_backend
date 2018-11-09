import coreapi
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Q
from rest_framework.exceptions import ParseError
from rest_framework.filters import BaseFilterBackend

from src.apps.withdrawal_point.models import WithdrawalPoint


class NearestItemsFilter(BaseFilterBackend):
    radius_param = 'radius'
    point_param = 'point'

    def get_filter_point(self, request):
        point_string = request.query_params.get(self.point_param, None)
        if not point_string:
            return None

        try:
            (longitude, latitude) = (float(n) for n in point_string.split(','))
        except ValueError:
            raise ParseError('Invalid geometry string supplied for parameter {0}'.format(self.point_param))

        p = Point(x=latitude, y=longitude)
        return p

    def filter_queryset(self, request, queryset, view):
        filter_field = getattr(view, 'distance_filter_field', None)
        radius = request.query_params.get(self.radius_param, None)
        point = self.get_filter_point(request)

        if not all((filter_field, radius, point)):
            return queryset

        # distance in meters
        try:
            dist = Distance(m=radius)
        except TypeError:
            raise ParseError('Invalid distance string supplied for parameter {0}'.format(self.radius_param))

        return queryset.filter(Q(**{'{}__distance_lt'.format(filter_field): (point, dist)}))

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name=self.radius_param,
                location='query',
                required=False,
                type='float',
                description='Search radius (in meters)'
            ),
            coreapi.Field(
                name=self.point_param,
                location='query',
                required=False,
                type='string',
                description='Comma separated string containing latitude and longitude values'
            ),
        ]


class WithdrawalPointBankFilter(BaseFilterBackend):
    bank_id_param = 'bank_id'

    def _get_filter_bank(self, request):
        bank_id_string = request.query_params.get(self.bank_id_param, None)
        print(bank_id_string)

        return bank_id_string

    def filter_queryset(self, request, queryset, view):
        bank_id = self._get_filter_bank(request)

        if not bank_id:
            return queryset

        return (
                queryset.filter(bank__id=bank_id) | queryset.filter(point_type=WithdrawalPoint.SHOP_POINT_TYPE)
        ).distinct()
