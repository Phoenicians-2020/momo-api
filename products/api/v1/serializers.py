from rest_framework import serializers

from products.models import Product, ProductType
from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'address',
            'province',
            'city',
            'postal_code',
            'country',
        )


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'name',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'location',
        )


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    product_photo = serializers.SerializerMethodField('get_profile_picture')
    product_type = serializers.SerializerMethodField('get_product_type_name')

    def get_profile_picture(self, obj):
        return obj.product_photo.url if obj.product_photo else None

    def get_product_type_name(self, obj):
        return obj.product_type.product_type_name if obj.product_type else None

    class Meta:
        model = Product
        fields = (
            'seller',
            'product_name',
            'product_type',
            'product_description',
            'product_photo',
            'price',
        )


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'
