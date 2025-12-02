from django.contrib.auth.models import User
from rest_framework import serializers
from .validators.base import load_validators, PasswordValidationError

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_password(self, value):
        validators = load_validators()
        errors = []
        for v in validators:
            try:
                v.validate(value, user=None)
            except PasswordValidationError as exc:
                # raise first meaningful error
                raise serializers.ValidationError({"message": exc.message, "code": exc.code})
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

