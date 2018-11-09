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


class WithdrawalPointBanksFilter(BaseFilterBackend):
    banks_id_param = 'bank_ids'

    def _replace_trash_from_str(self, string):
        symbols_to_replace = [',', ' ', '[', ']']

        for symbol in symbols_to_replace:
            if symbol in string:
                string = string.replace(symbol, '')

        return string

    def _convert_str_to_list(self, string):
        string = self._replace_trash_from_str(string)
        list_of_int = []

        for symbol in string:
            if not symbol.isnumeric():
                raise ParseError('{} contains non-numeric symbol - {}'.format(self.banks_id_param, symbol))

            list_of_int.append(int(symbol))

        return list_of_int

    def _get_filter_bank(self, request):
        bank_ids_string = request.query_params.get(self.banks_id_param, None)

        if not bank_ids_string:
            return None

        bank_ids_list = self._convert_str_to_list(bank_ids_string)

        return bank_ids_list

    def filter_queryset(self, request, queryset, view):
        bank_ids = self._get_filter_bank(request)

        if not bank_ids:
            return queryset

        return (
                queryset.filter(bank__id__in=bank_ids) | queryset.filter(point_type=WithdrawalPoint.SHOP_POINT_TYPE)
        ).distinct()

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name=self.banks_id_param,
                location='query',
                required=False,
                type='list',
                description='Bank ids list. Example: /api/withdrawalPoints/?bank_ids=[1,2,3] and ect.',
            ),
        ]
