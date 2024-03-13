from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, CustomUserInfo

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email',
                    'is_staff',)
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    model = CustomUserInfo
    list_display = ('user', 'height', 'bmi', 'classification')

admin.site.register(CustomUserInfo, UserInfoAdmin)
