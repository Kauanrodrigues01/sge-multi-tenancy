from django.db import models
from django.contrib.auth.models import User

class WebhookConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='webhook_config')
    webhook_url = models.URLField(max_length=255, blank=True, null=True, help_text="URL do Webhook")

    def __str__(self):
        return f"Configuração do Webhook para {self.user.username}"