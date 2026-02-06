from django.contrib import admin
from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor', 'vendor_email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description', 'vendor__email']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Store Information', {
            'fields': ('name', 'description', 'address')
        }),
        ('Vendor', {
            'fields': ('vendor',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    readonly_fields = ['created_at']
    
    def vendor_email(self, obj):
        return obj.vendor.email
    vendor_email.short_description = 'Vendor Email'
    
    # Quick filters
    list_filter = ['is_active', 'created_at', 'vendor__role']
    
    # Actions
    actions = ['approve_stores', 'deactivate_stores']
    
    def approve_stores(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} stores approved.")
    approve_stores.short_description = "Approve selected stores"
    
    def deactivate_stores(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} stores deactivated.")
    deactivate_stores.short_description = "Deactivate selected stores"




from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'product_count']
    search_fields = ['category_name']
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Total Products'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category', 'veg_flag', 'is_active', 'created_by', 'created_at']
    list_filter = ['category', 'veg_flag', 'is_active', 'created_at']
    search_fields = ['product_name', 'description']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Product Details', {
            'fields': ('product_name', 'description', 'product_image')
        }),
        ('Pricing & Category', {
            'fields': ('price', 'category', 'veg_flag')
        }),
        ('Status & Tracking', {
            'fields': ('is_active', 'created_by'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'created_by']
    
    # Automatically set created_by to current user
    def save_model(self, request, obj, form, change):
        if not change:  # Only on creation
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    
    # Actions
    actions = ['mark_as_veg', 'mark_as_non_veg', 'activate_products', 'deactivate_products']
    
    def mark_as_veg(self, request, queryset):
        queryset.update(veg_flag=True)
        self.message_user(request, f"{queryset.count()} products marked as vegetarian.")
    mark_as_veg.short_description = "Mark as Vegetarian"
    
    def mark_as_non_veg(self, request, queryset):
        queryset.update(veg_flag=False)
        self.message_user(request, f"{queryset.count()} products marked as non-vegetarian.")
    mark_as_non_veg.short_description = "Mark as Non-Vegetarian"
    
    def activate_products(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} products activated.")
    activate_products.short_description = "Activate selected products"
    
    def deactivate_products(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} products deactivated.")
    deactivate_products.short_description = "Deactivate selected products"