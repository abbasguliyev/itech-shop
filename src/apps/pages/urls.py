from django.urls import path
from apps.pages import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('index_partners_pagination/', views.IndexPartnersPaginationView.as_view(), name="index_partners_pagination_view"),

]