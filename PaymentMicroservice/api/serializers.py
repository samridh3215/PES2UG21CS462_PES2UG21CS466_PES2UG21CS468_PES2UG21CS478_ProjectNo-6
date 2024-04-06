# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Payment
 
# Create a model serializer
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Payment
        fields = ('payment_id', 'payment_amount')