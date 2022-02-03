from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug) 
        products= Product.objects.filter(category=categories, is_available=True) # query all the products filter by the categories
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True) # query all the products in the db that are available
        product_count = products.count()
    
    context = {
        'products': products, 
        'product_count': product_count, 
    }
    
    return render(request, 'store/store.html', context)


# objects es el manager, el manager permite generar los queries del modelo.

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context ={
        'product': product,
    }

    return render(request, 'store/product-detail.html', context)