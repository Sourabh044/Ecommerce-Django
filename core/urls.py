from django.shortcuts import HttpResponse
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views

def check(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path("", Home, name="home"),
    path("products/", ProductsView, name="products"),
    path("products/add-to-cart/<str:pk>",add_to_cart_view, name="add-to-cart"),
    path("products/buy/", OrderPlaceView, name="PlaceOrder"),
    path("products/buy/<str:pk>", OrderPlaceView, name="buy-now-single"),
    path("cart/", CartView, name="cart"),
    path("cart/<str:pk>", CartView, name="remove-cart"),
    path("myorders/", OrderListView, name="all-orders"),
    path("add-address/", AddressView, name="add-addresses"),
    path("address/", AddressListView, name="all-addresses"),
    path("address/<str:pk>", AddressListView, name="single-addresses"),
    path("login/", Login_view, name="login"),
    path("logout/", Logout_view, name="logout"),
    path("signup/", Signup_view, name="signup"),
    path("checkout/", Checkout, name="checkout"),

    path('token/', views.obtain_auth_token), #api token url
]
