from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

optional = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    name = models.CharField(_('Full Name of User'), blank=True, null=True, max_length=255)
    phone_number = models.CharField(max_length=11, **optional)

    def __str__(self):
        return self.first_name


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="location")
    address = models.CharField(max_length=255)
    province = models.CharField(_("Province"), max_length=50)
    city = models.CharField(_('City'), blank=True, null=True, max_length=255)
    postal_code = models.CharField(_('Postal Code'), max_length=10, default='8000')
    country = models.CharField(_('Country'), blank=True, null=True, max_length=255)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.address, self.city, self.province, self.postal_code)
