from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

class Contact(models.Model):
    first_name = models.CharField(_("ad"), max_length=255)
    last_name = models.CharField(_("soyad"), max_length=255)
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefon"), max_length=255)
    message = models.TextField(_("mesaj"))

    class Meta:
        verbose_name_plural = _("Kontaktlar")


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Company(models.Model):
    phone = models.CharField(_("telefon"), max_length=255)
    facebook_url = models.URLField(max_length = 500)
    tiktok_url = models.URLField(max_length = 500)
    instagram_url = models.URLField(max_length = 500)