from django.urls import path
from .views import order_create , order_confirmation

app_name = "ordersapp"

urlpatterns = [
    path('create',order_create,name="order_create"),#path for creating order
    path("confirmation/<int:order_id>",order_confirmation,name="order_confirmation"),
    #path for order confirmation
]