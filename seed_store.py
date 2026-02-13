import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Store
from accounts.models import User

def create_stores():
    # Fetch vendors we just created (filtering by username pattern)
    vendors = User.objects.filter(username__startswith='vendor_')

    if not vendors.exists():
        print("No vendors found! Please run seed_vendor.py first.")
        return

    for vendor in vendors:
        store_name = f"{vendor.username.replace('_', ' ').title()} Shop"
        
        # Check if this vendor already has a store to avoid duplicates
        if not Store.objects.filter(vendor=vendor).exists():
            Store.objects.create(
                name=store_name,
                description=f"Welcome to {store_name}. We offer the best products managed by {vendor.username}.",
                address=f"{random.randint(1, 999)} Marketplace Street, City Center",
                is_active=True,
                vendor=vendor
            )
            print(f"✅ Created Store: {store_name} for Vendor: {vendor.username}")
        else:
            print(f"⏩ Skipped: {vendor.username} already has a store.")

if __name__ == "__main__":
    create_stores()