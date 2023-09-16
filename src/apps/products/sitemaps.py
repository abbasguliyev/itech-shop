from django.contrib.sitemaps import Sitemap
from apps.products.models import Product

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    
    def items(self):
        return Product.objects.select_related('category').all()
    
    def lastmod(self, obj):
        return obj.updated