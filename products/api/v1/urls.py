from django.urls import include, path
from rest_framework import routers

from products.api.v1 import viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register('products', viewsets.ProductsViewSet, basename='search-products')
router.register('product-types', viewsets.ProductTypesViewSet, basename='product-types')

urlpatterns = [
    path("", include(router.urls)),
]
