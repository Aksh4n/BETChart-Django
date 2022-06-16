from django.urls import path 
from . import views
from transactions.views import BetMoneyView
urlpatterns = [
    path('game', views.game , name="game"),
    path("bet/", BetMoneyView.as_view(), name="bet_money"),

]
