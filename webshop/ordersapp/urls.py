from django.urls import path, include

from ordersapp.views import CustomerListView, AddingCustomerView

app_name = 'ordersapp'

urlpatterns = [
    path('customers/add/', AddingCustomerView.as_view(), name='customers_add'),
    path('customers/', CustomerListView.as_view(), name='customers')
]