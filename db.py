


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',  # The name of your MySQL database
        'USER': 'root',      # Your MySQL username (e.g., 'root')
        'PASSWORD': 'Madhu@12',  # Your MySQL password
        'HOST': '127.0.0.1',          # Or the IP address of your MySQL server
        'PORT': '3306',               # The default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # Recommended for data integrity
        }
    }
}




# from accounts.models import Product # Replace with your actual model name

# sample_products = [
#     {'name': 'MacBook Pro M3', 'category': 'Electronics', 'price': 1999, 'stock': 12},
#     {'name': 'Signature Linen Shirt', 'category': 'Apparel', 'price': 55, 'stock': 100},
#     {'name': 'Ceramic Vase Set', 'category': 'Home', 'price': 45, 'stock': 15},
#     {'name': 'Midnight Serum', 'category': 'Beauty', 'price': 85, 'stock': 30},
#     {'name': 'High-Waist Denim', 'category': 'Clothes', 'price': 70, 'stock': 45},
# ]

# for item in sample_products:
#     Product.objects.get_or_create(
#         name=item['name'],
#         defaults={'category': item['category'], 'price': item['price'], 'stock': item['stock']}
#     )

# print("Sample products loaded successfully!")
