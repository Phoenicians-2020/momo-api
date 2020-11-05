from django.urls import include, path
from rest_framework import routers

from users.api.v1 import viewsets

router = routers.DefaultRouter(trailing_slash=False)
router.register('', viewsets.SellerViewSet, basename='sellers')

urlpatterns = [
    path("", include(router.urls)),
]
