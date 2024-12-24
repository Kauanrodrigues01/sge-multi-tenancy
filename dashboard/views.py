import json
from django.shortcuts import render
from utils import metrics

def home(request):
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    
    context = {
        'page_dashboard_is_active': 'active',
        'products_metrics': metrics.get_products_metrics(),
        'sales_metrics': metrics.get_sales_metrics(),
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data)
    }
    return render(request, 'dashboard/home.html', context)