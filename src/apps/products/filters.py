import django_filters
from django import forms
from django.db.models import Q, Value
from django.db.models.functions import Concat
from apps.products.models import Product, Category

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'class': 'var-input',
        'name': 'name'
    }), required=False)
    category = django_filters.ModelChoiceFilter(queryset = Category.objects.all(), widget=forms.Select(attrs={
        'class': 'var-select',
        'placeholder': 'category',
        'name': 'category'
    }), required=False)

    class Meta:
        model = Product
        fields = {'name', 'category'}