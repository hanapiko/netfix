from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'field', 'price_per_hour', 'company_username', 'created_date']
    list_filter = ['field', 'created_date']
    search_fields = ['name', 'description', 'company_username__username']
    readonly_fields = ['created_date']
