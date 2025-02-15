import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from utils import metrics
from ai.models import AIResult
from services.agent import SGEAgent


@login_required
def home(request):
    agent = SGEAgent()
    agent.invoke()

    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()
    ai_result = AIResult.objects.first()
    if ai_result:
        ai_result = AIResult.objects.first().result

    context = {
        'page_dashboard_is_active': 'active',
        'products_metrics': metrics.get_products_metrics(),
        'sales_metrics': metrics.get_sales_metrics(),
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
        'ai_result': ai_result
    }

    return render(request, 'dashboard/home.html', context)
