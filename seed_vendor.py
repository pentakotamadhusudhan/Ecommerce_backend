import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from accounts.models import User

def create_vendors(n=50):
    for i in range(1, n + 1):
        username = f'vendor_{i}'
        email = f'vendor{i}@example.com'
        # Generate a dummy unique mobile number
        mobile_number = f'90000000{i:02d}' 
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=email,
                password='password123',
                mobile=mobile_number  # <--- Pass the unique mobile here
            )
            print(f"Created: {username} with mobile {mobile_number}")
        else:
            print(f"Skipped: {username} already exists")

if __name__ == "__main__":
    create_vendors(50)