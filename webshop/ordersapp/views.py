from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics

from ordersapp.models import Customer, Order
from ordersapp.serializers import CustomerSerializer, OrderSerializer


class AddCustomerView(LoginRequiredMixin, APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        message = {'message': 'customer not loaded'}
        obj = CustomerSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            message = {'message': 'Ok'}

        return Response(message)


class AddOrderView(LoginRequiredMixin, APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        message = {'message': 'order not added'}
        obj = OrderSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            message = {'message': 'Ok'}

        return Response(message)


class CustomerListView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Customer.objects.all().order_by()


class OrderListView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')
