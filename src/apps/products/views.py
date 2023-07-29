from django.shortcuts import render
from django.views.generic.list import ListView
from apps.products.models import Product

class ProductView(ListView):
    model = Product
    paginate_by = 10
    template_name = "products.html"
    context_object_name = "products"