from django import forms
from .models import Batch, Sale
class SaleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kg'].widget.attrs.update({'placeholder': 'Enter no. of kg'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Enter price'})
        self.fields['date'].widget.attrs.update({'placeholder': 'Enter date'})
        self.fields['customer_name'].widget.attrs.update({'placeholder': 'Enter customer name'})
        self.fields['customer_phone'].widget.attrs.update({'placeholder': 'Enter customer phone number'})
    class Meta:
        model = Sale
        fields = ('kg', 'price', 'date', 'customer_name', 'customer_phone')

class BatchForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kg'].widget.attrs.update({'placeholder': 'Enter no. of kg'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'Enter cost'})
        # self.fields['date_created'].widget.attrs.update({'placeholder': 'Enter date'})
        self.fields['vendor_name'].widget.attrs.update({'placeholder': 'Enter vendor name'})
        self.fields['vendor_phone'].widget.attrs.update({'placeholder': 'Enter vendor phone number'})
    class Meta:
        model = Batch
        fields = ('batch_name', 'date_created', 'cost', 'kg', 'price_per_kg', 'vendor_name','vendor_phone', 'close_account')