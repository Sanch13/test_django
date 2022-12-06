from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrders
from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrders.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrders.objects.all()
    serializer_class = OrderSerializer
