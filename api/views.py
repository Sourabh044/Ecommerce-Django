from api.serializers import CartSerializer, ProductSerializer
from core.models import Cart, Product
from rest_framework.decorators import api_view , authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self): #get products of the current user only.
        queryset = super().get_queryset()
        # self.request.user
        queryset = queryset.filter(user=self.request.user)
        return queryset


    def perform_create(self, serializer): #adding the current user in the model instance.
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs): # restricting from unauthorized deletion.
        instance = self.get_object()
        if request.user == instance.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)    


@api_view(["GET"])
def all_products(request): #getting all the products.

    serializer = ProductSerializer(
        Product.objects.all(), many=True, context={"request": request}
    )  #
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def all_cart_items(request):
    qs = Cart.objects.filter(user=request.user)
    return Response(CartSerializer(qs,many=True).data,status=status.HTTP_200_OK)