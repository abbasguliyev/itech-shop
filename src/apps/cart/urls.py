from django.urls import path
from apps.cart import views

urlpatterns = [
    path('', views.CartListView.as_view(), name="cart"),
    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
    path('delete/<int:pk>/', views.DeleteProdFromCartView.as_view(), name="delete_prod_from_cart"),
]