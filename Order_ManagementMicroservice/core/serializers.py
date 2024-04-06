# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import CartItem
 
# Create a model serializer
class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = CartItem
        fields = ('name', 'item_id', 'quantity', 'price')