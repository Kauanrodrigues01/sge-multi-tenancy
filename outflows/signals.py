from django.dispatch import receiver
from django.db.models.signals import post_save

from middlewares.thread_local_middleware import get_current_user
from .tasks import send_outflow_notify
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, created, **kwargs):
    try:
        user = get_current_user()
    except Exception:
        user = None
    send_outflow_notify.delay(instance.id, user.username, created)
