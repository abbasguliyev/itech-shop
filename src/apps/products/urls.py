from django.urls import path
from apps.products import views

urlpatterns = [
    path('', views.ProductView.as_view(), name="products"),
]