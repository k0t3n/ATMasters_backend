from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from src.apps.bank.models import Bank
from src.apps.bank.serializers import BankSerializer


class BankListView(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = PageNumberPagination
