from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(_("kateqoriya"), max_length=255)

    class Meta:
        verbose_name_plural = _("Kateqoriyalar")

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(_("şəkil"), upload_to="products/")
    price = models.DecimalField(_("qiymət"), decimal_places=2, max_digits=10)
    description = RichTextField(_("açıqlama"), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    class Meta:
        verbose_name_plural = _("Məhsullar")

    def __str__(self) -> str:
        return self.name