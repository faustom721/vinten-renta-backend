from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    last_used_company = serializers.SerializerMethodField()

    class Meta(object):
        model = CustomUser
        fields = "__all__"


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ("first_name", "last_name", "username")


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "ci",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = CustomUser.objects.create_user(
            username=self.validated_data.get("username"),
            ci=self.validated_data.get("ci"),
            first_name=self.validated_data.get("first_name"),
            last_name=self.validated_data.get("last_name"),
            password=self.validated_data.get("password"),
            email=self.validated_data.get("email"),
            phone=self.validated_data.get("phone"),
            is_active=False,
        )


class CustomJWTSerializer(TokenObtainPairSerializer):
    """Let the user obtain their token using their username or email in the email field"""

    def validate(self, attrs):
        credentials = {"username": "", "password": attrs.get("password")}

        user_obj = (
            CustomUser.objects.filter(email=attrs.get("username")).first()
            or CustomUser.objects.filter(username=attrs.get("username")).first()
        )
        if user_obj:
            credentials["username"] = user_obj.username

        return super().validate(credentials)
