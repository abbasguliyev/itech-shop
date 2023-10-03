from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.db.models import OuterRef, Subquery, Max, Min, When, Case, Value, F, Q, DecimalField
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

from apps.pages.models import Company

from apps.products.models import Product, Category, Discount, AttributeValues, Attributes, ProductColor
from apps.products import filters, enums


class ProductView(ListView):
    model = Product
    paginate_by = 5
    template_name = "products.html"
    context_object_name = "products"
    form_class = filters.ProductFilter

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset().annotate(
            discount_amount=Max(Case(
                When(Q(discounts__discount_type=enums.DiscountType.FIXED) & Q(discounts__is_active=True), then=F('price') - F('discounts__amount')),
                When(Q(discounts__discount_type=enums.DiscountType.PERCENTAGE) & Q(discounts__is_active=True), then=F('price') * F('discounts__amount') / 100),
                output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
            )
        )
        filtered_queryset = filters.ProductFilter(self.request.GET, queryset=queryset).qs
        return filtered_queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent=None).all()
        company = Company.objects.all().last()
        context['company'] = company

        # Filter the result
        filter = filters.ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter
        queryset = filter.qs.order_by('pk')

        # Paginate the results
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        if self.request.GET.get('category') is not None:
            context['current_category'] = Category.objects.filter(pk=self.request.GET.get('category')).last()
        else:
            context['current_category'] = None

        context['attribute_values'] = AttributeValues.objects.select_related('attribute').all()
        context['selected_attribute_values'] = [int(selected_attribute_value) for selected_attribute_value in self.request.GET.getlist('attribute_values')]
        context['search_name'] = self.request.GET.get('name')
        context['attribute_titles'] = Attributes.objects.all()
        
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name="product_detail.html"
    context_object_name = "product"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset().annotate(
            discount_amount=Max(Case(
                When(Q(discounts__discount_type=enums.DiscountType.FIXED) & Q(discounts__is_active=True), then=F('price') - F('discounts__amount')),
                When(Q(discounts__discount_type=enums.DiscountType.PERCENTAGE) & Q(discounts__is_active=True), then=F('price') * F('discounts__amount') / 100),
                output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
            )
        )
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.all().last()
        context['colors'] = ProductColor.objects.select_related('product').filter(product=self.get_object()).all()
        return context