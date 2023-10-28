from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.db.models import OuterRef, Subquery, Max, When, Case, Value, F, Q, DecimalField

from django.views.generic import TemplateView, View
from django.contrib import messages

from apps.products.models import Product
from apps.products import filters, enums

from apps.pages.models import Company

def add_to_cart(request):
    product_pk = request.POST.get("product")
    product = Product.objects.select_related("category").prefetch_related("attributes").filter(pk=product_pk).last()
    if product:
        if request.session.get("cart"):
            prod_list = request.session.get("cart")
            prod_list = set(prod_list)
            prod_list.add(product.pk)
            messages.success(request, "Məhsul səbətə əlavə edildi")
        else:
            prod_list = set()
            prod_list.add(product.pk)
            messages.success(request, "Məhsul səbətə əlavə edildi")
        request.session["cart"] = list(prod_list)
    return render(request, "htmx_cart.html")

class CartListView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        company = Company.objects.all().first()
        products = self.request.session.get("cart")
        product_instances = [Product.objects.select_related("category").prefetch_related("attributes").annotate(
            discount_amount=Max(Case(
                When(Q(discounts__discount_type=enums.DiscountType.FIXED) & Q(discounts__is_active=True), then=F('price') - F('discounts__amount')),
                When(Q(discounts__discount_type=enums.DiscountType.PERCENTAGE) & Q(discounts__is_active=True), then=F('price') * F('discounts__amount') / 100),
                output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
            )
        ).filter(pk=product_pk).last() for product_pk in products]
        price_list = [prod.price if prod.discount_amount is None else prod.discount_amount for prod in product_instances]
        total_price = sum(price_list)
        context["products"] = product_instances
        context["total_price"] = total_price
        context["company"] = company
        return context
    
    def get(self, request, *args: Any, **kwargs: Any):
        products = self.request.session.get("cart")
        if products == None:
            messages.info(request, "Səbətdə məhsul yoxdur!")
            return redirect("home")
        elif len(products) == 0:
            messages.info(request, "Səbətdə məhsul yoxdur!")
            return redirect("home")
        return super().get(request, *args, **kwargs)
    
class DeleteProdFromCartView(View):
    def post(self, request, pk):
        cart = request.session.get("cart")
        cart.remove(int(pk))
        request.session["cart"] = cart
        return redirect("cart")