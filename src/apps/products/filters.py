import django_filters
from django import forms
from django.db.models import Q, Value
from django.db.models.functions import Concat
from apps.products.models import Product, Category, Attributes, AttributeValues, ProductAttribute

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'class': 'var-input',
        'name': 'name'
    }), required=False)
    category = django_filters.ModelMultipleChoiceFilter(queryset = Category.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False, method='filter_category')
    attribute_values = django_filters.ModelMultipleChoiceFilter(queryset = AttributeValues.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False, method='filter_attribute_values')

    def filter_attribute_values(self, queryset, name, value):
        print(f"*******************************************{self.request=}")
        print(f"*******************************************{value=}")
        print(f"*******************************************{name=}")
        if value:
            queryset = queryset.filter(attributes__attribute_values__in=value)
        else:
            queryset = queryset
        return queryset
    
    def filter_category(self, queryset, name, value):
        if value:
            queryset = queryset.filter(Q(category__in=value) | Q(category__parent__in=value))
        else:
            queryset = queryset
        return queryset

    class Meta:
        model = Product
        fields = {'name', 'category'}