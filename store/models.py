from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Store(models.Model):
    vendor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="stores"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length= 30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'products_table'
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
