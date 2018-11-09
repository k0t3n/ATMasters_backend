from rest_framework import routers

from src.apps.withdrawal_point.views import WithdrawalPointListView
from src.apps.bank.views import BankListView
from src.apps.currency.views import CurrencyListView

router = routers.SimpleRouter()

router.register('withdrawalPoints', WithdrawalPointListView)
router.register('banks', BankListView)
router.register('currencies', CurrencyListView)

urlpatterns = router.urls
