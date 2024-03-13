from django.urls import path, include

from .views import CustomUserInfoListAPIView, CustomUserInfoCreateAPIView

urlpatterns = [
    path("user-info/", CustomUserInfoListAPIView.as_view(), name="user-info"),
    path("user-info/add/", CustomUserInfoCreateAPIView.as_view(), name="update-user-info"),
]