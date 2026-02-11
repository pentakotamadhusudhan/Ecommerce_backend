from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source="vendor.id")
    class Meta:
        model = Store
        fields = "__all__"

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    category = CatagorySerializer(read_only=True)
    
    # This allows you to still send an ID when creating a product
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(), 
        source='category', 
        write_only=True
    )
    class Meta:
        model = Product
        fields = '__all__'
        


from rest_framework import serializers
from .models import Product

class ProductDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'product_image', 'veg_flag', 'description', 'category_id']
        




class StoreProductSerializer(serializers.ModelSerializer):
    category = CatagorySerializer(read_only=True)

    class Meta:
        model = StoreProduct
        fields = [
            "id",
            "store",
            "product",
            "category",
            "is_active",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]
        depth=1