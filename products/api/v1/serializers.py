from rest_framework import serializers

from products.models import Product, ProductType


class ProductSerializer(serializers.ModelSerializer):
    product_photo = serializers.SerializerMethodField('get_profile_picture')

    def get_profile_picture(self, obj):
        return obj.product_photo.url if obj.product_photo else None

    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_type',
            'product_description',
            'product_photo',
            'product_location',
            'seller_address',
            'seller_name',
            'seller_email',
            'seller_phone_number',
            'price',
        )


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'
