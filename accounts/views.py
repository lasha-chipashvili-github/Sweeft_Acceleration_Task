from .models import CustomUserInfo
from .serializers import CustomUserInfoSerializer, CustomUserInfoCreateSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# Create your views here.
class CustomUserInfoListAPIView(generics.ListAPIView):
    serializer_class = CustomUserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CustomUserInfo.objects.filter(user=user)

class CustomUserInfoCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserInfoCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        height = float(self.request.POST.get('height'))
        current_weight = float(self.request.POST.get('current_weight'))
        custom_user_info = CustomUserInfo(user=user, height=height, current_weight=current_weight)
        custom_user_info.save()
        return Response("User Information is added!", status=status.HTTP_201_CREATED)

