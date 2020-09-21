from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('order-confirmed/', views.order_submit,name='order_submit'), #order submit code 1811
    path('myorders/', views.allorders,name='myorders'),
]