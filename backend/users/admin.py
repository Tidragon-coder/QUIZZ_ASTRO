from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Game", {"fields": ("xp",)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Game", {"fields": ("xp",)}),
    )
    list_display = ("username", "email", "xp", "is_staff", "is_superuser")
