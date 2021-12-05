from django import forms
from ordersapp.models import Order, Customer

from ordersapp.models import Customer, Order


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all().order_by('name'),
        label='Заказчик',
        empty_label='Заказчик не выбран',
    )
    order_total_cost = forms.IntegerField(
        label='Сумма заказа'
    )
    
