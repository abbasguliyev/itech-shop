from django.shortcuts import render
from apps.products.models import Product
from apps.services.models import Services


def index(request):
    products = Product.objects.all()[:3]
    services = Services.objects.all()[:3]
    context = {
        "products": products,
        "services": services
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')