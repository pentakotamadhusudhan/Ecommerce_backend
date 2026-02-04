from rest_framework import serializers
from .models import User
## user Login Serializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "mobile",
            "gender",
            "role",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            mobile=validated_data["mobile"],
            gender=validated_data.get("gender"),
            role=validated_data.get("role"),
            password=validated_data["password"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')


from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User

from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user_obj = User.objects.get(email=email)
            print("email")
            print(user_obj)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        user = authenticate(
            username=user_obj.username,  # Django expects username
            password=password
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        attrs['user'] = user
        return attrs
