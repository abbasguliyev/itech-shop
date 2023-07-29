from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Product(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    image = models.ImageField(_("şəkil"), upload_to="products/")
    price = models.DecimalField(_("qiymət"), decimal_places=2, max_digits=10)
    description = models.TextField(_("məlumat"))

    def __str__(self) -> str:
        return self.name