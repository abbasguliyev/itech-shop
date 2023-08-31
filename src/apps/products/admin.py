from django.contrib import admin
from apps.products.models import Product, Category, Attributes, Banner, Collection, Discount

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

@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value')
    list_display_links = ('id', 'title', 'value')
    list_filter = ('title',)
    search_fields = ('title', 'value')

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

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_active', 'created_at', 'end_date')
    list_display_links = ('id', 'title', 'slug')
    list_filter = ('is_active', 'title')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ['title']}