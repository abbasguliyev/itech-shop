from django.db import models
from django.utils.translation import gettext as _
from itech_shop.image_validator import compress


class Services(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    image = models.ImageField(_("şəkil"), upload_to="products/")

    class Meta:
        verbose_name_plural = _("Servislər")

    def save(self, *args, **kwargs):
        if self.image != None:
            new_image = compress(self.image)
            self.image = new_image

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name