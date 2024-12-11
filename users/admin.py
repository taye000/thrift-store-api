from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'city', 'country', 'profile_image', 'is_seller')}),
    )
    list_display = ('username', 'email', 'phone_number', 'is_seller', 'is_staff', 'is_active')
