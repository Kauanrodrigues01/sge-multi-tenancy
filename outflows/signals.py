import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
from datetime import datetime
from services.evolution import EvolutionAPI
from middlewares.thread_local_middleware import get_current_user
from utils.messages import create_outflow_message


logger = logging.getLogger(__name__)


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
                    
            evolution = EvolutionAPI()
            
            cost_price = instance.product.cost_price
            selling_price =  instance.product.selling_price
            quantity = instance.quantity
            
            data = {
                'product_name': instance.product.title,
                'quantity': quantity,
                'total_value': quantity * selling_price,
                'profit_value': quantity * (selling_price - cost_price),
                'username': user.username,
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S ')
            }
                        
            message = create_outflow_message(**data)
                                    
            evolution.send_text_message(
                text=message,
            )
            

    except Exception as e:
        logger.error(f"Failed: {str(e)}")
    