from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save, pre_save

from services.evolution import EvolutionAPI
from utils.messages import create_outflow_message
from middlewares.thread_local_middleware import get_current_user
from inflows.models import Inflow
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            total_cost_price = 0
            outflow_quantity = instance.quantity

            if outflow_quantity > instance.product.quantity:
                instance.delete()
                return

            try:
                with transaction.atomic():
                    inflows = Inflow.objects.filter(product=instance.product, quantity__gt=0).order_by('created_at')  # Ordenando para usar os inflows mais antigos primeiro

                    for inflow in inflows:
                        print(inflow.created_at)
                        inflow_quantity = inflow.quantity

                        if outflow_quantity > inflow_quantity:  # saida maior que entrada
                            inflow.quantity = 0
                            inflow.save()
                            outflow_quantity -= inflow_quantity
                            
                            # calcula o custo total
                            total_cost_price += inflow_quantity * inflow.cost_price

                        elif inflow_quantity > outflow_quantity:  # entrada maior que saida
                            inflow.quantity -= outflow_quantity
                            inflow.save()
                            
                            # calcula o custo total
                            total_cost_price += outflow_quantity * inflow.cost_price
                            break

                        else:  # entrada igual a saida
                            inflow.quantity = 0
                            inflow.save()
                            
                            # calcula o custo total
                            total_cost_price += inflow_quantity * inflow.cost_price
                            break
            except Exception as e:
                print(f'Erro ao processar a transação: {e}')
                raise
            finally:
                instance.total_cost_price = total_cost_price
                instance.save()


@receiver(pre_save, sender=Outflow)
def set_outflow_prices(sender, instance, **kwargs):
    """Antes de salvar um Outflow, armazena os preços do produto no momento da saída."""
    instance.cost_price = instance.product.cost_price
    instance.selling_price = instance.product.selling_price


# @receiver(post_save, sender=Outflow)
# def send_outflow_event(sender, instance, created, **kwargs):
#     try:
#         if created:
#             user = get_current_user()

#             evolution = EvolutionAPI()

#             cost_price = instance.product.cost_price
#             selling_price = instance.product.selling_price
#             quantity = instance.quantity

#             data = {
#                 'product_name': instance.product.title,
#                 'quantity': quantity,
#                 'total_value': quantity * selling_price,
#                 'profit_value': quantity * (selling_price - cost_price),
#                 'username': user.username,
#                 'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S ')
#             }

#             message = create_outflow_message(**data)

#             response = evolution.send_text_message(
#                 text=message,
#             )

#             if 'error' in response:
#                 print("ERRO NO ENVIO")
#                 print(response)

#             if response is None:
#                 print("ERRO NAS CONFIGURAÇÕES")

#             send_mail(
#                 subject='Nova Saída (SGE)',
#                 message='',
#                 from_email=f'SGE <{settings.DEFAULT_FROM_EMAIL}>',  # Fazendo dessa forma cria um tipo de "apelido" para o email
#                 recipient_list=[settings.MY_EMAIL],
#                 fail_silently=False,  # "Silencia" caso der erro não atrapalha a execução do codigo
#                 html_message=render_to_string('email/email_outflow.html', data)
#             )
#     except Exception as e:
#         return e
