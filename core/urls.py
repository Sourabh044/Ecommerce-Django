from django.shortcuts import HttpResponse
from django.urls import path, include
from .views import *


def check(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path("", Home, name="home"),
    path("products/", ProductsView, name="products"),
    path("products/buy/<str:pk>", BuyView, name="buy-now"),
    path("products/buy/", BuyView, name="buy-now"),
    path("cart/", CartView, name="cart"),
    path("cart/<str:pk>", CartView, name="remove-cart"),
    path("myorders/", OrderView, name="all-orders"),
    path("add-address/", AddressView, name="add-addresses"),
    path("address/", AddressListView, name="all-addresses"),
    path("address/<str:pk>", AddressListView, name="single-addresses"),
    path("login/", Login_view, name="login"),
    path("logout/", Logout_view, name="logout"),
    path("signup/", Signup_view, name="signup"),
]
