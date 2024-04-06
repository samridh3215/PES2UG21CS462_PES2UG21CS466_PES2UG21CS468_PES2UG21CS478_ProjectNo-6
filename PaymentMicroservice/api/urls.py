from django.urls import path, include

from .views import *

from rest_framework import routers

# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("<int:item_id>/",views.detail, name="detail"),
]