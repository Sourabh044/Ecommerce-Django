from api.serializers import ProductSerializer
from core.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets ,authentication, permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
@api_view(['GET'])
def all_products(request):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer = ProductSerializer(Product.objects.all(), many=True,context={"request": request}) #
    return Response(serializer.data)

