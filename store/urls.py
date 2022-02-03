from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    # convierte la categoria a un slug para poder filtrar por categoria y la agrego a la ruta
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail')

]
