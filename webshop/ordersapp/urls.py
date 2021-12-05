from django.urls import path, include

from ordersapp.views import CustomerListView, AddCustomerView, OrderListView, AddOrderView

app_name = 'ordersapp'

urlpatterns = [
    path('customers/add/', AddCustomerView.as_view(), name='customers_add'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/add/', AddOrderView.as_view(), name='orders_add'),
]
