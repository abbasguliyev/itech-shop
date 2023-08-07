from django.shortcuts import render
from django.views.generic.list import ListView
from apps.services.models import Services

class ServicesView(ListView):
    model = Services
    paginate_by = 10
    template_name = "services.html"
    context_object_name = "services"