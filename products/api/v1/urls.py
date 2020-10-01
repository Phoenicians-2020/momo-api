from django.urls import include, path
from rest_framework import routers

from products.api.v1 import viewsets

router = routers.DefaultRouter()
router.register('products', viewsets.ProductsViewSet, basename='products')
router.register('product-types', viewsets.ProductTypesViewSet, basename='product-types')
router.register('filter-products', viewsets.FilterProductsViewSet, basename='filter-products')

urlpatterns = [
    path("", include(router.urls)),
]
