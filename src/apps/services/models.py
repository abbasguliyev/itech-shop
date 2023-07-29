from django.db import models
from django.utils.translation import gettext as _

class Services(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    image = models.ImageField(_("şəkil"), upload_to="products/")

    def __str__(self) -> str:
        return self.name