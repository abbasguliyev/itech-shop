from collections.abc import Iterable
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
        ordering = ('pk',)
        default_permissions = []
        permissions = (
            ("view_category", "Mövcud kateqoriyalara baxa bilər"),
            ("add_category", "Kateqoriyalar əlavə edə bilər"),
            ("change_category", "Kateqoriyaları yeniləyə bilər"),
            ("delete_category", "Kateqoriyaları silə bilər")
        )

    def save(self, *args, **kwargs):
        try:
            new_icon = compress(self.icon)
            self.icon = new_icon
        except:
            pass
        finally:
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        if self.parent is not None:
            return f"{self.parent.name}/{self.name}/"
        return f"{self.name}/"

class Attributes(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    show_cart = models.BooleanField(_("Kartın üstünə gəldikdə göstərilsin"), default=False)

    class Meta:
        verbose_name_plural = _("Atributlar")
        ordering = ('pk',)
        default_permissions = []
        permissions = (
            ("view_attributes", "Mövcud attributlara baxa bilər"),
            ("add_attributes", "Attribut əlavə edə bilər"),
            ("change_attributes", "Attributları yeniləyə bilər"),
            ("delete_attributes", "Attributları silə bilər")
        )


    def __str__(self) -> str:
        return f"{self.title}"
    
class AttributeValues(models.Model):
    attribute = models.ForeignKey(Attributes, on_delete=models.SET_NULL, null=True, blank=True, related_name="values")
    value = models.CharField(_("dəyər"), max_length=255)

    class Meta:
        verbose_name_plural = _("Atribut Dəyərləri")
        ordering = ('pk',)
        default_permissions = []
        permissions = (
            ("view_attributevalues", "Mövcud attribut dəyərlərinə baxa bilər"),
            ("add_attributevalues", "Attribut dəyəri əlavə edə bilər"),
            ("change_attributevalues", "Attribut dəyərlərini yeniləyə bilər"),
            ("delete_attributevalues", "Attribut dəyərlərini silə bilər")
        )

    def __str__(self) -> str:
        return f"{self.attribute}: {self.value}"

class Product(models.Model):
    name = models.CharField(_("ad"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(_("qiymət"), decimal_places=2, max_digits=10)
    description = RichTextField(_("açıqlama"), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    class Meta:
        verbose_name_plural = _("Məhsullar")
        ordering = ('pk',)
        default_permissions = []
        permissions = (
            ("view_product", "Mövcud məhsullara baxa bilər"),
            ("add_product", "Məhsul əlavə edə bilər"),
            ("change_product", "Məhsulları yeniləyə bilər"),
            ("delete_product", "Məhsulları silə bilər")
        )
    
    def __str__(self) -> str:
        return self.name
     
class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = _("Məhsul Rəngləri")
        ordering = ('pk',)
        default_permissions = []
        permissions = (
            ("view_productcolor", "Mövcud məhsul rənglərinə baxa bilər"),
            ("add_productcolor", "Məhsul üçün rəng əlavə edə bilər"),
            ("change_productcolor", "Məhsul rənglərini yeniləyə bilər"),
            ("delete_productcolor", "Məhsul rənglərini silə bilər")
        )

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("şəkil"), upload_to="products/")

    class Meta:
        verbose_name_plural = _("Məhsul Şəkilləri")
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_productimage", "Mövcud məhsul şəkillərinə baxa bilər"),
            ("add_productimage", "Məhsul üçün şəkil əlavə edə bilər"),
            ("change_productimage", "Məhsul şəkillərini yeniləyə bilər"),
            ("delete_productimage", "Məhsul şəkillərini silə bilər")
        )

    def save(self, *args, **kwargs):
        if self.image != None:
            new_image = compress(self.image)
            self.image = new_image

        super().save(*args, **kwargs)

    
class ProductAttribute(models.Model):
    attribute_values = models.ManyToManyField(AttributeValues, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")

    class Meta:
        verbose_name_plural = _("Məhsul Atributları")
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_productattribute", "Mövcud məhsul attributlarına baxa bilər"),
            ("add_productattribute", "Məhsul üçün attribut əlavə edə bilər"),
            ("change_productattribute", "Məhsul attributlarını yeniləyə bilər"),
            ("delete_productattribute", "Məhsul attributlarını silə bilər")
        )

    
    def __str__(self) -> str:
        return f"{self.product.name}"

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
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_discount", "Mövcud endirimlərə baxa bilər"),
            ("add_discount", "Endirim əlavə edə bilər"),
            ("change_discount", "Endirimləri yeniləyə bilər"),
            ("delete_discount", "Endirimləri silə bilər")
        )


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
    
    class Meta:
        verbose_name_plural = _("Təkliflər")
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_collection", "Mövcud təkliflərə baxa bilər"),
            ("add_collection", "Təklif əlavə edə bilər"),
            ("change_collection", "Təklifləri yeniləyə bilər"),
            ("delete_collection", "Təklifləri silə bilər")
        )
    
class Banner(models.Model):
    title = models.CharField(_("başlıq"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(_("şəkil"), upload_to="banner/")
    is_active = models.BooleanField(_("aktiv"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = _("Banner")
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_banner", "Mövcud bannerlərə baxa bilər"),
            ("add_banner", "Banner əlavə edə bilər"),
            ("change_banner", "Bannerləri yeniləyə bilər"),
            ("delete_banner", "Bannerləri silə bilər")
        )

    def save(self, *args, **kwargs):
        if self.image != None:
            new_image = compress(self.image)
            self.image = new_image

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class HomePageProducts(models.Model):
    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name="home_page_products")
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if self.is_active == True:
            HomePageProducts.objects.prefetch_related('products').filter(is_active=True).update(is_active=False)
            self.is_active = True

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _("Ana Səhifəyə düşəcək məhsullar")
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_homepageproducts", "Ana səhifədəki məhsullara baxa bilər"),
            ("add_homepageproducts", "Ana səhifədə görünəcək məhsulları təyin edə bilər"),
            ("change_homepageproducts", "Ana səhifədə görünəcək məhsulları yeniləyə bilər"),
            ("delete_homepageproducts", "Ana səhifədə görünəcək məhsulları silə bilər")
        )