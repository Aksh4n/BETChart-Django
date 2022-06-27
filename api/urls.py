from django.urls import path
from . import views

urlpatterns = [

    path('price/',views.getData , name="price") , 
    path('add/',views.addData) , 
    path('pot/',views.potData , name="pot") , 
    path('ballance/',views.ballanceData , name="ballance") , 
    path('gmember/',views.gmemberData , name="gmember") , 
    path('rmember/',views.rmemberData , name="rmember") , 
    path('count/',views.countData , name="count") , 





]