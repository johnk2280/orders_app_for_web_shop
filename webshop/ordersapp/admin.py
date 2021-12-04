from django.contrib import admin

from ordersapp.models import Customer, Order


admin.site.register(Customer)
admin.site.register(Order)
