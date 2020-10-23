from django import forms
from django.contrib.auth.models import User
from . models import Order


class OrderShippingDetailForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('address', 'city', 'zip_code', 'country', 'phone', )

        
