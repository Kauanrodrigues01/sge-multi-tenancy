from django import forms
from .models import WebhookConfig

class WebhookConfigForm(forms.ModelForm):
    class Meta:
        model = WebhookConfig
        fields = ['webhook_url']
        widgets = {
            'webhook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Digite a URL do Webhook'}),
        }
