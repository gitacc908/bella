from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.product.models import Product


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = (
            'id', 'phone', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'write_only': True, 'style': 
                {
                    'input_type': 
                    'password', 'placeholder': 'Password'
                }
            }
        }
    
    def validate(self, validated_data):
        password1 = validated_data.get('password')
        password2 = validated_data.get('password2')
        if len(password1) < 8 or len(password2) < 8:
            raise serializers.ValidationError(
                f"Длина пароля должна быть больше 8 символов.")
        elif password1 == password2:
            if len(password1) < 8 or len(password2) < 8:
                raise serializers.ValidationError(
                    f"Длина пароля должна быть больше 8 символов.")
            return validated_data
        raise serializers.ValidationError(
            f"Введенные вами пароли не совпадают, попробуйте еще.")
    
    def create(self, validated_data):
        phone_number = validated_data.get('phone').replace("+", "")
        if phone_number.isdigit():
            user = User.objects.create_user(
                phone = f'+{phone_number}',
                password = validated_data.get('password'),
                first_name = validated_data.get('first_name'),
                last_name = validated_data.get('last_name')
            )
            return user
        raise serializers.ValidationError(
            f"Должны быть только цифры.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name')


class UserBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('favorite_products',)
