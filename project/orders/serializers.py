from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrders


class OrderSerializer(ModelSerializer):
    
    class Meta:
        model = SalesOrders
        fields = ['amount', 'description']
