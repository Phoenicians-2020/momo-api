from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from users.forms import UserCreateForm
from users.models import (
    Location,
    Seller,
    User
)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "is_staff"
    ]

    search_fields = [
        "name",
        "email",
    ]

    fieldsets = [
        [
            'System Users', {
                'fields': [
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password',
                    'is_staff',
                    'groups'
                ]
            }
        ]
    ]

    def save_model(self, request, obj, form, change):
        obj.name = obj.first_name + ' ' + obj.last_name
        super().save_model(request, obj, form, change)

        return obj.name


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone_number"
    ]

    search_fields = [
        "name",
        "email",
        "phone_number"
    ]

    fieldsets = [
        [
            'System Users', {
                'fields': [
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number'
                ]
            }
        ]
    ]

    def save_model(self, request, obj, form, change):
        obj.name = obj.first_name + ' ' + obj.last_name
        super().save_model(request, obj, form, change)

        return obj.name


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "seller",
        "address",
        "city",
        "province",
        "postal_code",
    ]

    search_fields = [
        "address",
        "city",
        "province",
        "postal_code",
    ]
