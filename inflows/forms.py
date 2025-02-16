from django import forms

from products.models import Product
from suppliers.models import Supplier
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def __init__(self, *args, user=None,**kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['product'].queryset = Product.objects.filter(user=user)
            self.fields['supplier'].queryset = Supplier.objects.filter(user=user)
        else:
            self.fields['product'].queryset = Product.objects.none()
            self.fields['supplier'].queryset = Supplier.objects.none()
