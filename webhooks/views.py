
from django.shortcuts import render, redirect
from .forms import WebhookConfigForm
from django.contrib.auth.decorators import login_required
from .models import WebhookConfig
from django.http import JsonResponse

@login_required
def edit_webhook_config(request):
    try:
        webhook_config = request.user.webhook_config
        print(f"WebhookConfig encontrado: {webhook_config}")
    except WebhookConfig.DoesNotExist:
        webhook_config = None
        print("WebhookConfig não encontrado para o usuário.")
    
    if request.method == 'POST':
        print("Método POST recebido.")
        if webhook_config is None:
            print("Nenhuma configuração de webhook encontrada. Criando uma nova configuração.")
            form = WebhookConfigForm(request.POST)
        else:
            print("Configuração de webhook existente. Atualizando.")
            form = WebhookConfigForm(request.POST, instance=webhook_config)
        
        if form.is_valid():
            print('Formulário válido. Salvando dados.')
            # Adiciona o usuário autenticado antes de salvar
            webhook_config = form.save(commit=False)
            webhook_config.user = request.user  # Aqui associamos o usuário atual
            webhook_config.save()
            print("Configuração de webhook salva com sucesso.")
            return redirect('dashboard:home')  # Redirecione para uma página de sucesso ou outra
        else:
            print(f"Formulário inválido. Erros: {form.errors}")
    else:
        print("Método GET recebido. Carregando formulário.")
        form = WebhookConfigForm(instance=webhook_config)
    
    return render(request, 'webhooks/edit_webhook_config.html', {'form': form})
