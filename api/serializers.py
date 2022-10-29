from core.models import Cart, Product
from rest_framework import serializers  
from drf_extra_fields.fields import Base64ImageField

class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Product
        fields = ['id','name','brand','description','price','image']



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','product','quantity','order_status','user',)