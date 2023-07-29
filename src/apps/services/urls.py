from django.urls import path
from apps.services import views

urlpatterns = [
    path('', views.services_list, name="services"),
]