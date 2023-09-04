from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from itech_shop.image_validator import compress
from apps.products import enums

class Category(models.Model):
    name = models.CharField(_("kateqoriya"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.SET_NULL, null=True, blank=True)
    icon = models.ImageField(_("icon"), upload_to="category/", null=True, blank=True)

    class Meta:
        verbose_name_plural = _("Kateqoriyalar")

    def save(self, *args, **kwargs):
        if self.icon != None:
            new_icon = compress(self.icon)
            self.icon = new_icon

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Attributes(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    value = models.CharField(_("dəyər"), max_length=255)
    show_cart = models.BooleanField(_("Kartın üstünə gəldikdə göstərilsin"), default=False)

    class Meta:
        verbose_name_plural = _("Atributlar")

    def __str__(self) -> str:
        return f"{self.title}: {self.value}"

class Product(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(_("şəkil"), upload_to="products/")
    price = models.DecimalField(_("qiymət"), decimal_places=2, max_digits=10)
    description = RichTextField(_("açıqlama"), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    attributes = models.ManyToManyField(Attributes, related_name="products")

    class Meta:
        verbose_name_plural = _("Məhsullar")

    def save(self, *args, **kwargs):
        if self.image != None:
            new_image = compress(self.image)
            self.image = new_image

        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Discount(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    discount_type = models.CharField(_("endirim növü"), max_length=50, choices=enums.DiscountType.choices, default=enums.DiscountType.FIXED)
    amount = models.DecimalField(_("məbləğ"), decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    product = models.ManyToManyField(Product, related_name="discounts")
    is_active = models.BooleanField(_("aktiv"), default=True)

    class Meta:
        verbose_name_plural = _("Endirim")

    def __str__(self) -> str:
        return self.title
    
class Collection(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, related_name="collections")
    is_active = models.BooleanField(_("aktiv"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
    
class Banner(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(_("şəkil"), upload_to="banner/")
    is_active = models.BooleanField(_("aktiv"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title