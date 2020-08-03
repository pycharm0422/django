from django.urls import path
from . import views

urlpatters = [
    path('', views.customer, name='customer'),
    path('dashboard/', views.dashboard, name='customer'),
]