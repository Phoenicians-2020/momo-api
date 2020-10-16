from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from users.forms import UserCreateForm
from users.models import User, Location


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone_number",
        "is_staff"
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
                    'username',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'password',
                    'groups'
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
        "user",
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
