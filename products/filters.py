from django_filters import rest_framework as filters

from products.models import Product, ProductType


class ProductFilter(filters.FilterSet):
    """
    Custom filter class for filtering products by product type
    """
    product_type = filters.CharFilter(field_name='product_type__product_type_name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['product_type']
