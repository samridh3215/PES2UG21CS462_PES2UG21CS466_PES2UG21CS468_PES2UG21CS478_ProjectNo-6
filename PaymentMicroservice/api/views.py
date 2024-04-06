from rest_framework import viewsets

# import local data
from .serializers import PaymentSerializer
from .models import Payment

# create a viewset


class PaymentsViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Payment.objects.all()

	# specify serializer to be used
	serializer_class = PaymentSerializer