from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (  # 기존 필드에 추가
        ('Additional Info', {'fields': ('profile_image', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (  # 사용자 추가 폼에 추가
        ('Additional Info', {'fields': ('profile_image', 'bio')}),
    )