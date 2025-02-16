from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inflows')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
