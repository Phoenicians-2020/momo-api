from django.db import models
from django.utils.translation import ugettext_lazy as _

optional = {
    'null': True,
    'blank': True
}


class ProductType(models.Model):
    product_type_name = models.CharField(max_length=255, **optional)
    datetime_created = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    datetime_updated = models.DateTimeField(verbose_name=_("last updated"), auto_now=True)

    def __str__(self):
        return self.product_type_name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    product_name = models.CharField(max_length=255, **optional)
    product_description = models.CharField(max_length=255, **optional)
    product_photo = models.ImageField(upload_to='product_images/', **optional)
    product_location = models.CharField(max_length=255, **optional)
    seller_address = models.CharField(max_length=255, **optional)
    seller_name = models.CharField(max_length=255, **optional)
    seller_email = models.CharField(max_length=255, **optional)
    seller_phone_number = models.CharField(max_length=11, **optional)
    price = models.DecimalField(max_digits=20, decimal_places=8, **optional)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name = "Product",
        verbose_name_plural = "Products"
