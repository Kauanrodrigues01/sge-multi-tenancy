from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
from services.notify import Notify
from datetime import datetime
from django.contrib.auth.models import User
from middlewares.thread_local_middleware import get_current_user


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
        if created:
            user = get_current_user()
            
            notify = Notify(user=user)
            
            product = instance.product
            cost_price = instance.product.cost_price
            selling_price = instance.product.selling_price
            quantity = instance.quantity
            total_value = quantity * selling_price
            profit = quantity * (selling_price - cost_price)
            
            
            data = {
                'event_type': 'create_outflow',
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S '),
                'product': product.title,
                'product_cost_price': float(cost_price),
                'product_selling_price': float(selling_price), 
                'quantity': quantity,
                'description': instance.description,
                'total_value': total_value,
                'profit': float(profit)
            }
            
            notify.send_outflow_event(data=data)
    except:
        pass