from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from src.apps.bank.views import BankListView
from src.apps.currency.views import CurrencyListView
from src.apps.subway.views import SubwayStationsListView
from src.apps.withdrawal_point.views import WithdrawalPointListView

router = routers.SimpleRouter()

router.register('withdrawalPoints', WithdrawalPointListView)
router.register('banks', BankListView)
router.register('currencies', CurrencyListView)
router.register('subwayStations', SubwayStationsListView)

api_urls = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/swagger', include('src.apps.swagger.urls')),
    path('api/', include(api_urls)),
]
