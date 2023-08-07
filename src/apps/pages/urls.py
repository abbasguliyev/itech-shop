from django.urls import path
from apps.pages import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]