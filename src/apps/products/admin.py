from django.contrib import admin
from apps.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    list_filter = ('name',)
    search_fields = ('name', 'price')
