from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, CustomUserInfo, UserWeigth

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email',
                    'username',
                    'is_staff',)
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)


class UserWeigthAdmin(admin.ModelAdmin):
    model = UserWeigth
    list_display = ('user', 'date')


admin.site.register(UserWeigth, UserWeigthAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    model = CustomUserInfo
    list_display = ('user', 'sex', 'height', 'bmi', 'classification')

admin.site.register(CustomUserInfo, UserInfoAdmin)
