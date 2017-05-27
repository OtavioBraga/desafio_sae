from django import forms

from .models import Product, Purchase


class NewProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name',)

class NewPurchaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['value'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['purchase_date'].widget.attrs['class'] = 'form-control'
        self.fields['purchase_date'].widget.attrs.update(
            {'data-provide': 'datepicker'}
        )

    class Meta:
        model = Purchase
        fields = ('product', 'quantity', 'value', 'purchase_date')