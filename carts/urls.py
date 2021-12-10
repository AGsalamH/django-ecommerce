from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_cart),
    path('add/', views.add_cart),
]
