import json

from django.core.serializers import serialize

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from products.models import Product, ProductType
from products.api.v1.serializers import ProductSerializer, ProductTypeSerializer


class ProductsViewSet(viewsets.ViewSet):
    """
    Handles api endpoints for products
    """

    @swagger_auto_schema(tags=['Products'])
    def list(self, request):
        """
        Display all products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=['Products'])
    def retrieve(self, request, pk=None):
        """
        Display specific product by id
        """
        if Product.objects.filter(id=pk).exists():
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FilterProductsViewSet(viewsets.ViewSet):
    """
    Handles api endpoint for filter products by product type
    """
    lookup_field = 'product_type_id'

    @swagger_auto_schema(tags=['Products'])
    def retrieve(self, request, *args, **kwargs):
        """
        Display list of filtered products by product type
        """
        product_type_id = kwargs.get('product_type_id', None)
        product_type = ProductType.objects.get(id=product_type_id)
        products = Product.objects.filter(product_type=product_type).distinct()

        serializer = json.loads(serialize('json', products))

        return Response(list(serializer), status=status.HTTP_200_OK)


class ProductTypesViewSet(viewsets.ViewSet):
    """
    Handles api endpoints for product types
    """

    @swagger_auto_schema(tags=['Product Types'])
    def list(self, request):
        """
        Display all product types
        """
        product_types = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_types, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
