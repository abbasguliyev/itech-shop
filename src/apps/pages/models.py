from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from itech_shop.image_validator import compress

class Contact(models.Model):
    first_name = models.CharField(_("ad"), max_length=255)
    last_name = models.CharField(_("soyad"), max_length=255)
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefon"), max_length=255)
    message = models.TextField(_("mesaj"))

    class Meta:
        verbose_name_plural = _("Kontakt mesajları")


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Company(models.Model):
    phone = models.CharField(_("telefon"), max_length=255)
    facebook_url = models.URLField(max_length = 500)
    tiktok_url = models.URLField(max_length = 500)
    instagram_url = models.URLField(max_length = 500)

    class Meta:
        verbose_name_plural = _("Şirkət məlumatları")

class Partners(models.Model):
    name = models.CharField(_("adı"), max_length=255)
    logo = models.ImageField(_("logo"), upload_to="partners/")

    class Meta:
        verbose_name_plural = _("Partnyorlar")

    def save(self, *args, **kwargs):
        if self.logo != None:
            new_logo = compress(self.logo)
            self.logo = new_logo

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name