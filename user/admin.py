from django.contrib import admin
from main.models import AppUser

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'field_of_work', 'first_name', 'last_name', 'date_joined']
    list_filter = ['field_of_work', 'date_joined', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']
