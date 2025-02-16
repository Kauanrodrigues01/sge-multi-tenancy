from django.db import models
from django.contrib.auth.models import User


class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suppliers')
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name = 'Fornecedores'
        ordering = ['name']

    def __str__(self):
        return self.name
