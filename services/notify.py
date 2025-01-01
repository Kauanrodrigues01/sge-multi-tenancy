from webhooks.models import WebhookConfig
import requests

class Notify:
    
    def __init__(self, user=None):
        self.__url = None 
        
        if user:
            webhook_config = WebhookConfig.objects.filter(user=user).first()
            if webhook_config and webhook_config.webhook_url:
                self.__url = webhook_config.webhook_url

    def send_outflow_event(self, data):
        if not self.__url:
            print("Webhook URL não configurada. Evento não enviado.")
            return None
        
        response = requests.post(
            url=self.__url,
            json=data
        )
        
        return response
    
    def send_inflow_event(self, data):
        if not self.__url:
            print("Webhook URL não configurada. Evento não enviado.")
            return None
        
        response = requests.post(
            url=self.__url,
            json=data
        )
        
        return response
