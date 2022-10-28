from django.shortcuts import HttpResponse
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views

def check(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path("", ProductsView, name="home"),
    path("products/", ProductsView, name="products"),
    path("signup/", Signup_view, name="signup"),
    path("login/", Login_view, name="login"),
    path("add-address/", AddressView, name="add-addresses"),
    path("address/", AddressListView, name="all-addresses"),
    path("address/<str:pk>", AddressListView, name="single-addresses"),
    path("products/add-to-cart/<str:pk>",add_to_cart_view, name="add-to-cart"),
    path("add-to-cart/<str:pk>",add_to_cart_view, name="add-to-cart"),
    path("cart/", CartListView, name="cart"),
    path("cart/<str:pk>", CartListView, name="remove-cart"),
    path("checkout/", Checkout, name="checkout"),
    path("checkout/<str:pk>", Checkout, name="checkout"),
    path("products/buy/", OrderPlaceView, name="PlaceOrder"),
    path("products/buy/<str:pk>", OrderPlaceView, name="buy-now-single"),
    path("myorders/", OrderListView, name="all-orders"),
    path("myorders/<str:pk>", OrderListView, name="all-orders"),
    path("logout/", Logout_view, name="logout"),

    path('token/', views.obtain_auth_token), #api token url
]
