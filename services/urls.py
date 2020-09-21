from django.urls import path
from . import views

urlpatterns = [
    path('',views.services_product,name='serv-list'),
    path('<int:id>/',views.services_detail, name='serv-detail'),
    path('new/',views.ServicesCreateView.as_view(),name='serv-add'),
]