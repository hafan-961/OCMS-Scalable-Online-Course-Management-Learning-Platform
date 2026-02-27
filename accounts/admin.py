from django.contrib import admin

# Register your models here.
from .models import accounts

@admin.register(accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('-created_at',)

