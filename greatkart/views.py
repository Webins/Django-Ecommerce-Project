from django.shortcuts import render

from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True) # query all the products in the db that are available

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)

