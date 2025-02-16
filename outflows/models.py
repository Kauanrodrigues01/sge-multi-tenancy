from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Outflow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Saída'
        verbose_name_plural = 'Saídas'
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
