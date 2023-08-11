from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from apps.products.models import Product, Category
from apps.products import filters

from apps.pages.models import Company

class ProductView(ListView):
    model = Product
    paginate_by = 10
    template_name = "products.html"
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        filtered_queryset = filters.ProductFilter(self.request.GET, queryset=queryset).qs
        return filtered_queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
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
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name="product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.all().last()
        return context