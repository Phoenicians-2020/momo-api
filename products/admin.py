from django.contrib import admin


from products.models import (
    ProductType,
    Product
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product_name",
        "product_type",
        "price"
    ]

    search_fields = [
        "product_name",
        "product_type",
    ]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product_type_name",
        "datetime_created",
        "datetime_updated"
    ]

    search_fields = [
        "product_type_name"
    ]
