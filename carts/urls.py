from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='carts'),
    path('add_cart/<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('delete_cart/<int:product_id>/', views.delete_from_cart, name='delete_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart_item, name='remove_cart'),
]
