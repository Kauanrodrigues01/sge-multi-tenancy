from datetime import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from services.evolution import EvolutionAPI
from utils.messages import create_outflow_message
from .models import Outflow


@shared_task
def send_outflow_notify(instance_id, user_username, created):
    try:
        if created:
            instance = Outflow.objects.select_related('product').get(id=instance_id)

            evolution = EvolutionAPI()

            cost_price = instance.product.cost_price
            selling_price = instance.product.selling_price
            quantity = instance.quantity

            data = {
                'product_name': instance.product.title,
                'quantity': quantity,
                'total_value': quantity * selling_price,
                'profit_value': quantity * (selling_price - cost_price),
                'username': user_username,
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }

            message = create_outflow_message(**data)

            evolution.send_text_message(
                text=message,
            )

            send_mail(
                subject='Nova Saída (SGE)',
                message='',
                from_email=f'SGE <{settings.DEFAULT_FROM_EMAIL}>',  # Fazendo dessa forma cria um tipo de "apelido" para o email
                recipient_list=[settings.MY_EMAIL],
                fail_silently=False,  # "Silencia" caso der erro não atrapalha a execução do codigo
                html_message=render_to_string('email/email_outflow.html', data)
            )

            return 'Success notification'
    except Exception as e:
        return f"Failed notification: {str(e)}"
