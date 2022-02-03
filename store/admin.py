from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_date', 'is_available')
    ordering = ('price', 'stock', 'is_available', '-created_date')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)