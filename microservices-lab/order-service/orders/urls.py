from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.orders_list),
    path('orders/<int:id>', views.order_detail),
]
