from django.db import models
from django.conf import settings

# 1. Using the setting for the User model is correct
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


class ProductCategory(models.Model):  # Fixed typo: Category (singular is standard)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):  # Naming convention: Singular (Product, not ProductsModel)
    product_name = models.CharField(max_length=50)
    
    # 2. Changed to DecimalField for currency precision
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # 3. Explicitly named upload_to
    product_image = models.ImageField(upload_to='productImages/', null=True, blank=True)
    
    # 4. Added mandatory on_delete
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products")
    
    veg_flag = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    # 5. Fixed reference to User and added on_delete
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # 6. Swapped auto_now logic
    created_at = models.DateTimeField(auto_now_add=True) # Set on creation
    updated_at = models.DateTimeField(auto_now=True)     # Updates on every save
    
    def __str__(self):
        return self.product_name




# models.py

class StoreProduct(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="store_products"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_stores"
    )
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="product_category")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField(default=0)
    original_price = models.FloatField(default=0.0)
    discount_price= models.FloatField(default=0.0)
    class Meta:
        unique_together = ("store", "product")
        verbose_name = "Store Product"
        verbose_name_plural = "Store Products"

    def __str__(self):
        return f"{self.store.name} - {self.product.product_name}"





class EventLog(models.Model):

    EVENT_TYPES = [
        ("product_click", "Product Click"),
        ("category_click", "Category Click"),
        ("store_click", "Store Click"),
        ("page_view", "Page View"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)

    product_id = models.CharField(max_length=200, null=True, blank=True)
    category_id = models.CharField(max_length=200, null=True, blank=True)
    store_id = models.CharField(max_length=200, null=True, blank=True)

    device_id = models.CharField(max_length=200, null=True, blank=True)
    session_id = models.CharField(max_length=200, null=True, blank=True)

    metadata = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["event_type"]),
            models.Index(fields=["product_id"]),
            models.Index(fields=["category_id"]),
            models.Index(fields=["store_id"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.event_type} - {self.user}"