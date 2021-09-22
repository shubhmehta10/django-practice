from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='images/profile.png',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'), 
        ('Out door','Out door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'), 
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.product.name
