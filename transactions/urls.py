from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView
from .views import BetMoneyView , BetMoneyView2
from . import views


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("bet/", BetMoneyView.as_view(), name="bet_money"),
    path("betgreen/", BetMoneyView2.as_view(), name="betgreen"),






]
