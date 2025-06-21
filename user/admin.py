from django.contrib import admin
from .models import User, Customer, Company

# Admin configuration for the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ("id", "username", "email")


# Admin configuration for the Company model
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ("user", "field")


# Admin configuration for the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ("user", "birth")
