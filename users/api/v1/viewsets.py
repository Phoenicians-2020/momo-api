from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from products.models import Seller
from products.api.v1.serializers import SellerSerializer


@swagger_auto_schema(tags=['Sellers'])
class SellerViewSet(viewsets.ModelViewSet):
    """
    Handles api endpoints for sellers
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filter_backends = ()
