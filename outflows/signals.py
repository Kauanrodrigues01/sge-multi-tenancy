from django.dispatch import receiver
from django.db.models.signals import post_save

from .tasks import send_outflow_notify
from .models import Outflow

from time import sleep

@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, created, **kwargs):
    send_outflow_notify.delay(instance.id, created)
