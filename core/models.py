from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4(),editable=False)
    name = models.CharField(max_length = 256, blank=False,null = False)

    def __str__(self):
        return self.name
class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4(),editable=False)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length = 256, blank=False,null = False)
    brand = models.ForeignKey( Brand,on_delete=models.CASCADE)
    description = models.TextField(max_length=500,blank=True,default='No Description')
    price = models.FloatField(blank=False,null=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    user = models.OneToOneField (User,on_delete=models.CASCADE)
    item = models.ManyToManyField(Item,blank=True)
    def __str__(self) -> str:
        return str(self.user)


class Order(models.Model):
    product = models.ManyToManyField(Item)
    order_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    Cart = models.ForeignKey(Cart,on_delete = models.CASCADE, null = True)
    def __str__(self):
        return str(f'{self.order_by} {self.created} id: {self.id}')
