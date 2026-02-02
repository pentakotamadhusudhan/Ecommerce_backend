from rest_framework import serializers
from .models import User
## user Login Serializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'role',   # 👈 user-type
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', User.Role.CUSTOMER)
        )
        return user


## user update serializer
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_role(self, value):
        if value in ['ADMIN', 'MANAGER', 'EXECUTIVE', 'STAFF', 'SUPPORT']:
            raise serializers.ValidationError(
                "You cannot register with this role."
            )
        return value

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
