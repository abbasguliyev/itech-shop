from typing import Any, Dict
from django.views.generic.list import ListView
from apps.services.models import Services
from apps.pages.models import Company

class ServicesView(ListView):
    model = Services
    paginate_by = 10
    template_name = "services.html"
    context_object_name = "services"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        company = Company.objects.all().last()
        context['company'] = company
        return context