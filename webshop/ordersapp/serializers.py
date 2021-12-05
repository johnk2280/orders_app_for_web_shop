import datetime

from rest_framework import serializers

from ordersapp.models import Customer, Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'name',
            'gender',
        )

    def save(self, **kwargs):
        customer = Customer()
        customer.name = self.validated_data['name']
        customer.gender = self.validated_data['gender']
        customer.save()


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = (
            'customer',
            # 'created_at',
            'total_cost',
        )

    def save(self, **kwargs):
        customer = Customer()
        customer.name = self.validated_data['name']
        customer.gender = self.validated_data['gender']

        order = Order()
        order.customer = customer
        # order.created_at = self.validated_data['created_at']
        order.total_cost = self.validated_data['total_cost']
        customer.save()
        order.save()
        return order
