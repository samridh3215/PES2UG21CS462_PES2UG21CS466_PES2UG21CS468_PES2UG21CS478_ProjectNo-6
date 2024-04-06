# cart_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.index, name='index'),
    #path('cart/add/', CartItemCreate.as_view(), name='add-to-cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
