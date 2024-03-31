from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Item,CartItem

# Create your views here.
def index(request):
    item= list(Item.objects.all())
    #item= Item.objects.order_by("-item_id")[:5]
    return render(request, "core/index.html",{"item": item})

@csrf_exempt
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart_item, created = CartItem.objects.get_or_create(item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'core/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')