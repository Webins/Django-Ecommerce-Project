from django.shortcuts import render, redirect, get_object_or_404
from carts.models import Cart, CartItem

from store.models import Product

# Create your views here.

"""Get the id of the currect cart or create one"""
def _get_cart_id(request):
    cart_id = request.session.session_key
    
    if not cart_id:
        cart_id = request.session.create()
    
    return cart_id


""" Add the current product to the cart """
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_get_cart_id(request)) 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_get_cart_id(request))

    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity = 1)
        cart_item.save()
    
    return redirect('carts')

""" delete the current product to the cart """
def delete_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  
    
    return redirect('carts')

""" remove the entire cart item"""
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

   
    cart_item.delete()  
    
    return redirect('carts')



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity

    except CartItem.DoesNotExist:
        pass 
    
    tax = (total * 2) / 100
    grand_total = total + tax

    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grand_total" : grand_total
    }

    return render(request, 'store/cart.html', context)
