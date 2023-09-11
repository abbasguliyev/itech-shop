from django.contrib import admin
from django import forms

from apps.products.models import Product, Category, AttributeValues, Attributes, Banner, Collection, Discount, ProductAttribute

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    list_filter = ('name',)
    search_fields = ('name', 'price')
    prepopulated_fields = {"slug": ['name']}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ['name']}

@admin.register(AttributeValues)
class AttributeValuesAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value')
    list_filter = ('value',)
    search_fields = ('value',)

@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_active', 'created_at')
    list_display_links = ('id', 'title', 'slug')
    list_filter = ('is_active', 'title')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ['title']}

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discount_type', 'amount', 'created_at', 'end_date', 'is_active')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'title', 'end_date')
    search_fields = ('title',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "product":
            # İlgili özelliği seçmek için bir dropdown menü oluşturun
            kwargs["widget"] = admin.widgets.FilteredSelectMultiple(
                db_field.verbose_name,
                is_stacked=False,
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_active', 'created_at', 'end_date')
    list_display_links = ('id', 'title', 'slug')
    list_filter = ('is_active', 'title')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ['title']}

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "products":
            # İlgili özelliği seçmek için bir dropdown menü oluşturun
            kwargs["widget"] = admin.widgets.FilteredSelectMultiple(
                db_field.verbose_name,
                is_stacked=False,
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "attribute_values":
            # İlgili özelliği seçmek için bir dropdown menü oluşturun
            kwargs["widget"] = admin.widgets.FilteredSelectMultiple(
                db_field.verbose_name,
                is_stacked=False,
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

