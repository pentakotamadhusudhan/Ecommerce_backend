from rest_framework import serializers
from .models import Product, Order,Store


class StoreSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source="vendor.id")
    class Meta:
        model = Store
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
