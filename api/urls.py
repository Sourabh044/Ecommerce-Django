from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("allproducts", all_products, name="api-products"),

]
urlpatterns += router.urls