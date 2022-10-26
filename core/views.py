from django.shortcuts import HttpResponse, redirect, render
from .models import *
from django.db.models import F

# Create your views here.


def Home(request):
    return render(request, "base.html")


def ProductsView(request, pk=None):
    if not pk:
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})


def CartView(request, pk=None):
    if not pk:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "cart.html", {"cart": cart, "status": cart.exists()})
    else:
        cart = Cart.objects.get(id=pk)
        cart.delete()
        return redirect("cart")


def BuyView(request, pk=None, **kwargs): # also order place view
    if not pk:
        user = request.user
        if not address.objects.filter(user=user).exists():
            return redirect("addresses")
        order = Order.objects.create(order_by=user)
        try:
            location = address.objects.get(default=True)
            order.address = location
        except Exception as e:
            print(e)
            location = address.objects.filter(user=user)[:1]
            order.address = location[0]
        Total = 0
        for item in Cart.objects.filter(user=user):
            order.cart.add(item)
            order.total = order.total+item.product.price
        order.save()
        return redirect('all-orders')

    user = request.user
    product = Product.objects.get(id=pk)
    if Cart.objects.filter(user_id=user, product=product).exists():
        Cart.objects.filter(user=user, product=product).update(
            quantity=F("quantity") + 1
        )
    else:
        Cart.objects.create(user=user, product=product)
    return redirect("cart")


def OrderView(request, pk=None):
    if not pk:
        orders = Order.objects.filter(order_by=request.user)
        return render(request, "order.html", {"orders": orders})

def AddressView(request,pk=None):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pincode = request.POST.get('pincode')
        landmark = request.POST.get('landmark')
        # address.objects.create(landmark=landmark,lat=lat,lng=lng,phone=phone,email=email,pincode=pincode,user=user)
        return redirect('alladdresses')
    if not pk:
        user = request.user
        adresses = address.objects.filter(user=user)
        if not adresses.exists():
            return HttpResponse('addaddresses')
        return render(request,'add-address.html',{'adresses':adresses})