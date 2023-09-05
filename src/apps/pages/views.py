from typing import Any, Dict
import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.core.paginator import Paginator

from apps.pages.models import Contact, Company, Partners
from apps.products.models import Product, Category, Banner, Collection
from apps.services.models import Services
from apps.pages.forms import ContactForm

class IndexView(ListView):
    model = Product
    paginate_by = 5
    template_name = "home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.all()
        company = Company.objects.all().last()
        categories = Category.objects.select_related('parent').all()
        partners = Partners.objects.all()[:3]
        banners = Banner.objects.filter(is_active=True)
        collection = Collection.objects.prefetch_related('products').filter(is_active=True, end_date__lte=datetime.datetime.today()).order_by("pk").last()
        if collection is not None:
            if collection.products.all() is not None:
                collection_prods = list(collection.products.order_by("pk").all())
            else:
                collection_prods = list()
        else:
            collection_prods = list()
        context['services'] = services
        context['company'] = company
        context['categories'] = categories
        context['partners'] = partners
        context['banners'] = banners
        context['collection'] = collection
        context['collection_prods'] = collection_prods
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.all().last()
        context['company'] = company
        return context

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, "contact.html", context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız müvəffəqiyyətlə göndərildi")
            return redirect('home')
        else:
            messages.error(request, "Mesajınızı göndərərkən xəta baş verdi")
            return redirect('home')
    

class IndexPartnersPaginationView(ListView):
    model = Partners
    paginate_by = 5
    template_name = "partners_index_pagination.html"
    context_object_name = "partners"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partners = Partners.objects.all()
        paginator = Paginator(partners, self.paginate_by)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        partners = paginator.page(page)
        context["page_obj"] = page_obj
        return context
    