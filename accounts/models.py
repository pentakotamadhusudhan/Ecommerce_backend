from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EXECUTIVE = "EXECUTIVE", "Executive"
        MANAGER = "MANAGER", "Manager"
        STAFF = "STAFF", "Staff"
        CUSTOMER = "CUSTOMER", "Customer"
        SUPPORT = "SUPPORT", "Customer Support"
        VENDOR = "VENDOR", "Vendor"
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"

        
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        default=Gender.MALE
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_manager(self):
        return self.role == self.Role.MANAGER

    def is_customer(self):
        return self.role == self.Role.CUSTOMER
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # 🔐 encrypts password
        user.save()
        return user

