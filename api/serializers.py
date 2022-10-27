from core.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    def get_image_url(self,product):
        if not product.image.url:
            return None
        else:
            request = self.context['request']
            image_url = product.image.url
            return request.build_absolute_uri(image_url)

    class Meta:
        model = Product
        fields = ['id','image_url','name','brand','description','price',]