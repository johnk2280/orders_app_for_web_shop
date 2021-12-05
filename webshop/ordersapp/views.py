from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework import generics

from ordersapp.models import Customer, Order
from ordersapp.serializers import CustomerSerializer, OrderSerializer


class AddingCustomerView(APIView):
    permission_classes = (BasePermission, )

    def post(self, request):
        message = {'message': 'customer not loaded'}
        obj = CustomerSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            message = {'message': 'Ok'}

        return Response(message)


class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (BasePermission, )

    def get_queryset(self):
        return Customer.objects.all().order_by()