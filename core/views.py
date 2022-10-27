from django.shortcuts import HttpResponse, redirect, render
from .models import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import make_password
from django.db.models import F

from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, "base.html")


def ProductsView(request, pk=None):
    if not pk:
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})


def CartView(request, pk=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not pk:
        cart = Cart.objects.filter(user=request.user)
        cart = cart.filter(order_status=False)
        return render(request, "cart.html", {"cart": cart.filter(order_status=False), "status": cart.exists()})
    else:
        cart = Cart.objects.get(id=pk)
        cart.delete()
        return redirect("cart")


def OrderPlaceView(request, pk=None ,**kwargs):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not address.objects.filter(user=user).exists():
        return redirect("add-addresses")
    order = Order.objects.create(order_by=user)
    try:
        location = address.objects.get(default=True)
        order.address = location
    except Exception as e:
        print(e)
        location = address.objects.filter(user=user)[:1]
        order.address = location[0]
    if pk:
        product = Product.objects.get(id=pk)
        cart = Cart.objects.create(user=user,product=product)
        order.cart.add(cart)
        order.total = product.price
        order.save()
        return redirect("all-orders")
    Total = 0
    for item in Cart.objects.filter(user=user):
        order.cart.add(item)
        item.order_status = True
        item.save() 
        order.total = order.total + item.product.price
    order.save()
    return redirect("all-orders")

    

def add_to_cart_view(request,pk=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not pk:
        return redirect('products')
    product = Product.objects.get(id=pk)
    if Cart.objects.filter(user_id=user, product=product).exists():
        Cart.objects.filter(user=user, product=product).update(
            quantity=F("quantity") + 1
        )
        cart = Cart.objects.filter(user_id=user, product=product)
        print(cart)
        messages.info(request, f'{product.name} added to your cart| quantity:{cart[0].quantity}')
    else:
        Cart.objects.create(user=user, product=product)
        messages.info(request, f'{product.name} added to your cart')
    return redirect("products")   


def OrderListView(request, pk=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not pk:
        orders = Order.objects.filter(order_by=request.user)
        return render(request, "order.html", {"orders": orders})


def AddressView(request, pk=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        print(request.POST)
        user = request.user
        lat = request.POST.get("lat")
        lng = request.POST.get("lng")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        pincode = request.POST.get("pincode")
        landmark = request.POST.get("landmark")
        address.objects.create(
            landmark=landmark,
            lat=float(lat),
            lng=float(lng),
            phone=phone,
            email=email,
            pincode=pincode,
            user=user,
        )
        return redirect("cart")
    return render(request, "add-address.html")


def AddressListView(request, pk=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if not pk:
        user = request.user
        addresses = address.objects.filter(user=user)
        if not addresses.exists():
            return render(request, "add-address.html")
        return render(request, "address.html", {"addresses": addresses})


def Login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'login.html')


def Logout_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('home')


def Signup_view(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password'] 
       User.objects.create(username=username,password=make_password(password))
       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('home')
       return redirect('home')
    return render(request,'signup.html')



def Checkout(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    cart = Cart.objects.filter(user=user)
    if cart.exists():
        cart = Cart.objects.filter(order_status=False)
        if cart.exists():
            total = 0
            for item in cart:
                total +=item.product.price
            addresses = address.objects.filter(user=user)
            return render(request,'checkout.html',{'cart':cart,'total':total,'addresses':addresses})
        return HttpResponse('No Orderable items in Your Cart')
    return HttpResponse('No Orderable items in Your Cart')