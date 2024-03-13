from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from .models import CustomUserInfo
class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomUserInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserInfo
        fields = ["user", "height", "current_weight"]

class CustomUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserInfo
        fields = ["user", "height", "current_weight", "date", "bmi", "classification"]
