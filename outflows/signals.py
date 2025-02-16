from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from services.evolution import EvolutionAPI
from middlewares.thread_local_middleware import get_current_user
from utils.messages import create_outflow_message
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
        if created:
            user = get_current_user()

            evolution = EvolutionAPI()

            cost_price = instance.product.cost_price
            selling_price = instance.product.selling_price
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

            response = evolution.send_text_message(
                text=message,
            )

            if 'error' in response:
                print("ERRO NO ENVIO")
                print(response)

            if response is None:
                print("ERRO NAS CONFIGURAÇÕES")

            send_mail(
                subject='Nova Saída (SGE)',
                message='',
                from_email=f'SGE <{settings.DEFAULT_FROM_EMAIL}>',  # Fazendo dessa forma cria um tipo de "apelido" para o email
                recipient_list=[settings.MY_EMAIL],
                fail_silently=False,  # "Silencia" caso der erro não atrapalha a execução do codigo
                html_message=render_to_string('email/email_outflow.html', data)
            )
    except Exception as e:
        return e
