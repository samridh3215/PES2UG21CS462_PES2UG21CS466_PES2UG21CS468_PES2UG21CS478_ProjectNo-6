# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import ItemSerializer
from .models import Item

# create a viewset


class ItemsViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Item.objects.all()

	# specify serializer to be used
	serializer_class = ItemSerializer



# from django.shortcuts import render, get_object_or_404
# from django.http import Http404

 
# from .models import Item

# def index(request):
#     latest_item_list= Item.objects.order_by("-item_id")[:5]
#     context = {"latest_item_list": latest_item_list,}
#     return render(request, "core/index.html",context)

# def detail(request, item_id):
#     item= get_object_or_404(Item, pk=item_id)
#     return render(request, "core/detail.html",{"item": item})
