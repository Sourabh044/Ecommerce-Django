# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, default="No Description")
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.name} | {self.quantity}"


PAYMENT_MEHTHODS = (("COD", "COD"), ("PREPAID", "PREPAID"))


class Order(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    cart = models.ManyToManyField(Cart)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    total = models.FloatField(default= 0,blank=True,null=True)
    payment_method = models.CharField(
        choices=PAYMENT_MEHTHODS, max_length=10, blank=True, null=True, default="COD"
    )
    address = models.ForeignKey(
        "address", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return str(
            f"{self.delivered} | {self.order_by} | {self.created} | {self.payment_method}"
        )


class address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    lat = models.FloatField(blank=True,null=True)
    lng = models.FloatField(blank=True,null=True)
    latlng = models.PointField()
    pincode = models.CharField(max_length=6)
    landmark = models.TextField(max_length=256)
    default = models.BooleanField(default=False)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        # point = Point(self.lng, self.lat)
        print('here')
        self.latlng = Point(self.lng, self.lat)
        super(address, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.pincode}"

    
# class Dummy(models.Model):
#     f = models.FloatField()

