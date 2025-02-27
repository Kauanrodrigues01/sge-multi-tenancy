from django.db import models
from django.contrib.auth.models import User

from brands.models import Brand
from inflows.models import Inflow
from categories.models import Category


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def quantity(self):
        inflows = Inflow.objects.filter(product=self).aggregate(
            total_quantity=models.Sum('quantity')
        )
        return inflows['total_quantity'] or 0
