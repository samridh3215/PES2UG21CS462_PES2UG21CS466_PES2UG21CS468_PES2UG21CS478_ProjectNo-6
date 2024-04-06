# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Item
 
# Create a model serializer
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Item
        fields = ('name', 'item_id', 'quantity', 'price')