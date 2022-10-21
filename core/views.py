from django.shortcuts import HttpResponse, redirect, render
from .models import *

# Create your views here.


def Home(request):
    return render(request, "base.html")


def ProductsView(request, pk=None):
    if not pk:
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})
        
# order = Order.objects.create


def CartView(request):
    cart = Cart.objects.get_or_create(user=request.user)
    cart = cart[0].item.all()  # rename to products to debug
    # print(cart.exists()) # To check if there is something in the Cart
    # print(cart.item.all().values_list())
    # for i in cart.item.all():
    #     print(i.product.id)
    return render(
        request, "cart.html", {"cart": cart,'status':cart.exists()}
    )  # add products to context to debug



def BuyView(request, pk=None, **kwargs): 
    if not pk:
        user = request.user
        order = Order.objects.get_or_create(order_by=user)
        return HttpResponse(order[0])
    
    user= request.user
    product = Product.objects.get(id=pk)
    item = Item.objects.create(product=product,quantity = 1)
    cart = Cart.objects.get_or_create(user=user)
    cart[0].item.add(item)
    return redirect('cart')

    


    
    