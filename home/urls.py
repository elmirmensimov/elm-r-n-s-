from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('orders/', views.order_list, name='order_list'),
    path('index/', views.index, name='index'),
]

