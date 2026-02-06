from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User  # Ensure this matches your app's User model

# --- 1. Branding Customization ---
admin.site.site_header = "Local BABA"
admin.site.site_title = "Local BABA Admin"
admin.site.index_title = "Welcome to Local BABA Portal"

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Added 'role_icon' to show an icon in the list view as requested
    list_display = ['email', 'mobile', 'role_icon', 'gender', 'is_active', 'date_joined']
    list_filter = ['role', 'gender', 'is_active', 'date_joined']
    search_fields = ['email', 'mobile', 'first_name', 'last_name']
    ordering = ['-date_joined']
    list_per_page = 25
    
    # 2. Corrected Template Path (Matches templates/admin/pie_chart.html)
    change_list_template = "admin/pie_chart.html"
    
    # --- 3. Custom Method for Role Icon ---
    def role_icon(self, obj):
        if obj.role == 'VENDOR':
            return format_html('🏪 <span style="color:#C5A08E; font-weight:bold;">Vendor</span>')
        elif obj.role == 'CUSTOMER':
            return format_html('🛒 <span>Customer</span>')
        return obj.role
    role_icon.short_description = 'Role'

    # --- 4. Fieldsets ---
    fieldsets = (
        ('🔐 Authentication', {
            'fields': ('email', 'password')
        }),
        ('👤 Personal Info', {
            'fields': ('first_name', 'last_name', 'mobile', 'gender')
        }),
        ('🎭 Role & Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('📅 Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )
    
    # Note: If your model is a Custom User, 'add_fieldsets' must be set
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password', 'role', 'gender', 'first_name', 'last_name'),
        }),
    )
    
    readonly_fields = ['date_joined', 'last_login']
    
    # --- 5. Actions ---
    actions = ['activate_users', 'deactivate_users', 'make_vendors', 'make_customers']
    
    @admin.action(description='✅ Activate selected users')
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users activated.", level='success')
    
    @admin.action(description='❌ Deactivate selected users')
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users deactivated.", level='warning')
    
    @admin.action(description='🏪 Convert to Vendors')
    def make_vendors(self, request, queryset):
        queryset.update(role='VENDOR')
        self.message_user(request, "Role updated to Vendor.", level='info')
    
    @admin.action(description='🛒 Convert to Customers')
    def make_customers(self, request, queryset):
        queryset.update(role='CUSTOMER')
        self.message_user(request, "Role updated to Customer.", level='info')

    # Load FontAwesome if needed for the status icons
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css',)
        }