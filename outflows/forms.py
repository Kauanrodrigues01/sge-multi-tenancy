from django import forms
from django.core.exceptions import ValidationError

from products.models import Product
from . import models


class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['product'].queryset = Product.objects.filter(user=user)
        else:
            self.fields['product'].queryset = Product.objects.none()

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity
