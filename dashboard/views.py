from django.shortcuts import render
from utils.metrics import get_products_metrics, get_sales_metrics

def home(request):
    context = {
        'page_dashboard_is_active': 'active',
        'products_metrics': get_products_metrics(),
        'sales_metrics': get_sales_metrics()
    }
    return render(request, 'dashboard/home.html', context)