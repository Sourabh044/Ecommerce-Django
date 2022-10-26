from django.shortcuts import HttpResponse
from django.urls import path, include
from .views import *


def check(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path("", Home, name="check"),
    path("products/", ProductsView, name="products"),
    path("products/buy/<str:pk>", BuyView, name="buy-now"),
    path("products/buy/", BuyView, name="buy-now"),
    path("cart/", CartView, name="cart"),
    path("cart/<str:pk>", CartView, name="remove-cart"),
    path("myorders/", OrderView, name="all-orders"),
    path("add-address/", AddressView, name="addaddresses"),
    path("all-address/", AddressView, name="alladdresses"),
]
