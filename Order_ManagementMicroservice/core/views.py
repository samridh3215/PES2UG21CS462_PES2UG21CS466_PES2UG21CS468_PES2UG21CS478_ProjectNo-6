import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import CartItemSerializer
from .models import CartItem
import os

url_for_items = "http://" + os.environ.get('ITEMSERVICE_SERVICE_HOST') + os.environ.get('ITEMSERVICE_SERVICE_PORT') + "/api/items/"
url_for_payment = "http://" + os.environ.get('ORDERSERVICE_SERVICE_HOST') + os.environ.get('ORDERSERVICE_SERVICE_PORT') + '/api/payments/'

# url_for_items = 'http://localhost:8000/api/items/'
# url_for_payment = 'http://localhost:8080/api/payments/'

# url_for_items = 'http://item-microservice:8000/api/items/'
# url_for_payment = 'http://payment-microservice:8080/api/payments/'

# Create your views here.
def index(request):
    # item= list(Item.objects.all())
    # #item= Item.objects.order_by("-item_id")[:5]
    # return render(request, "core/index.html",{"item": item})
    response = requests.get(url_for_items)
    items = response.json()
    # return render(request, "core/index.html",{"item": items})
    return JsonResponse(items, safe=False)

@csrf_exempt
def add_to_cart(request, item_id):
    item = requests.get(url_for_items+"{}/".format(item_id)).json()
    # item = Item.objects.get(pk=item_id)
    cart_item, created = CartItem.objects.get_or_create(item_id=item['item_id'], name=item['name'], price=item['price'])
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    response = requests.patch(url_for_items+"{}/".format(item_id), data={'quantity': item['quantity']-1})
    return redirect('view_cart')

def view_cart(request):
    cart_items = [item for item in CartItem.objects.all()]
    # data = serializers.serialize('json', cart_items, fields=('name', 'price', 'quantity'))
    data = CartItemSerializer(cart_items, many=True).data
    total_price = sum(item.price * item.quantity for item in cart_items)
    print(total_price)
    # return render(request, 'core/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})
    return JsonResponse({'cart_items': data, 'total_price': total_price}, safe=False)

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    item = requests.get(url_for_items+"{}/".format(cart_item.item_id)).json()
    response = requests.patch(url_for_items+"{}/".format(cart_item.item_id), data={'quantity': item['quantity'] + cart_item.quantity})
    cart_item.delete()
    return redirect('view_cart')

def checkout(request):
    cart_items = [item for item in CartItem.objects.all()]
    total_price = sum(item.price * item.quantity for item in cart_items)
    response = requests.post(url_for_payment, data={'payment_amount': total_price})
    for item in cart_items:
        item.delete()
    return redirect('view_cart')

