from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Inflow


# @receiver(post_save, sender=Inflow)
# def update_product_quantity(sender, instance, created, **kwargs):
#     if created:
#         if instance.quantity > 0:
#             product = instance.product
#             product.quantity += instance.quantity
#             product.save()


@receiver(pre_save, sender=Inflow)
def set_inflow_prices(sender, instance, **kwargs):
    """Antes de salvar um Inflow, armazena os preços do produto no momento da entrada."""
    if not instance.pk:
        instance.cost_price = instance.product.cost_price
        instance.selling_price = instance.product.selling_price
