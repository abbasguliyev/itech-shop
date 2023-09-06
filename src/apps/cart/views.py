from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from apps.products.models import Product
from apps.pages.models import Company

def add_to_cart(request):
    product_pk = request.POST.get("product")
    product = Product.objects.select_related("category").prefetch_related("attributes").filter(pk=product_pk).last()
    if product:
        if request.session.get("cart"):
            prod_list = request.session.get("cart")
            prod_list = set(prod_list)
            prod_list.add(product.pk)
        else:
            prod_list = set()
            prod_list.add(product.pk)

        request.session["cart"] = list(prod_list)
    return redirect("home")

class CartListView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        company = Company.objects.all().first()
        products = self.request.session.get("cart")
        product_instances = [Product.objects.select_related("category").prefetch_related("attributes").filter(pk=product_pk).last() for product_pk in products]
        price_list = [prod.price for prod in product_instances]
        total_price = sum(price_list)
        context["products"] = product_instances
        context["total_price"] = total_price
        context["company"] = company
        return context
    
    def get(self, request, *args: Any, **kwargs: Any):
        products = self.request.session.get("cart")
        if products == None:
            return redirect("home")
        elif len(products) == 0:
            return redirect("home")
        return super().get(request, *args, **kwargs)
    
class DeleteProdFromCartView(View):
    def post(self, request, pk):
        cart = request.session.get("cart")
        cart.remove(int(pk))
        request.session["cart"] = cart
        return redirect("cart")