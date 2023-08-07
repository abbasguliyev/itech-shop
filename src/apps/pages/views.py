from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from apps.pages.models import Contact, Company
from apps.products.models import Product
from apps.services.models import Services
from apps.pages.forms import ContactForm

def index(request):
    products = Product.objects.all()[:3]
    services = Services.objects.all()[:3]
    contact_form = ContactForm()
    company = Company.objects.all().last()
    context = {
        "products": products,
        "services": services,
        "contact_form": contact_form,
        "company": company
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')

class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız müvəffəqiyyətlə göndərildi")
            return redirect('home')
        else:
            messages.error(request, "Mesajınızı göndərərkən xəta baş verdi")
            return redirect('home')
    