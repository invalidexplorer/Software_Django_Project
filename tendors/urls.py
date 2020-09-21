from django.urls import path
from . import views

urlpatterns = [
    path('tendor-list/',views.TendorListView, name='tendor_list'),
    path('new/', views.TendorCreateView.as_view(), name='tendor_new'),
]