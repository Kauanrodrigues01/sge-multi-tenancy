from products.models import Product
from outflows.models import Outflow
from django.utils.formats import number_format, date_format
from django.db.models import Sum, F
from django.utils.timezone import localdate
from datetime import timedelta, date as dt

def get_products_metrics():    
    products_metrics_data = Product.objects.aggregate(
        total_quantity=Sum('quantity'),
        total_cost_price=Sum(F('cost_price') * F('quantity')),
        total_selling_price=Sum(F('selling_price') * F('quantity')) # Ele percorre linha por linha, o F obtém os valores de cost_price e quantity, realiza a multiplicação entre eles e, com o uso do Sum, adiciona o resultado ao valor inicial 0, acumulando o total de produto em produto.
    )
    
    total_quantity = products_metrics_data['total_quantity'] or 0
    total_cost_price = products_metrics_data['total_cost_price'] or 0
    total_selling_price = products_metrics_data['total_selling_price'] or 0
    total_profit = total_selling_price - total_cost_price
    
    return dict(
        total_quantity=total_quantity,
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True)
    )
    
    
def get_sales_metrics():
    total_sales = Outflow.objects.count()

    sales_data = Outflow.objects.aggregate(
        total_products_sold=Sum('quantity'),
        total_sales_value=Sum(F('product__selling_price') * F('quantity')),
        total_sales_cost=Sum(F('product__cost_price') * F('quantity')) # Apenas para calcular o lucro
    )

    total_products_sold = sales_data['total_products_sold'] or 0
    total_sales_value = sales_data['total_sales_value'] or 0
    total_sales_cost = sales_data['total_sales_cost'] or 0 # Apenas para calcular o lucro
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )
    
    
def get_daily_sales_data():
    today = localdate()
    dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    values = []

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=str(date)
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    # Formata as datas apenas no final
    formatted_dates = [date_format(date, format='d/m') for date in dates]

    return dict(
        dates=formatted_dates,
        values=values,
    )
    
    
def get_daily_sales_quantity_data():
    today = localdate()
    dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    values = list()
    
    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=str(date)).count()
        values.append(sales_quantity)
        
    dates = [date_format(date, format='d/m') for date in dates]
    
    return dict(
        dates=dates,
        values=values
    )
        
