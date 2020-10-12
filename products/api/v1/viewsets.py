import json

from django.core.serializers import serialize
from django.utils.decorators import method_decorator

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from products.api.v1.serializers import ProductSerializer, ProductTypeSerializer
from products.filters import ProductFilter
from products.models import Product, ProductType


# class ProductsViewSet(viewsets.ViewSet):
#     """
#     Handles api endpoints for products
#     """

#     @swagger_auto_schema(tags=['Products'])
#     def list(self, request):
#         """
#         Display all products
#         """
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     @swagger_auto_schema(tags=['Products'])
#     def retrieve(self, request, pk=None):
#         """
#         Display specific product by id
#         """
#         if Product.objects.filter(id=pk).exists():
#             product = Product.objects.get(id=pk)
#             serializer = ProductSerializer(product)

#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(tags=['Products'])
class ProductsViewSet(viewsets.ModelViewSet):
    """
    Handles api endpoints:
        1. Display list of products
        2. Get specific product by id
        3. Display list of products depending on search value (fields are: product name, product type name, seller name, seller email)
        4. Display filtered list by product name
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('product_name', 'product_type__product_type_name', 'seller_name', 'seller_email', 'product_description',)
    filter_fields = ('product_type',)
    filter_class = ProductFilter


class ProductTypesViewSet(viewsets.ViewSet):
    """
    Handles api endpoints for product types
    """

    @swagger_auto_schema(tags=['Product Types'])
    def list(self, request):
        """
        Display list of product types
        """
        product_types = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_types, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
