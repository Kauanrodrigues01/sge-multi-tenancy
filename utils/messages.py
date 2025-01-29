from django.utils.formats import number_format


outflow_message = '''
Olá, uma nova saída foi registrada no SGE. Feita pelo usuário: *{}*

Produto: *{}*
Quantidade: *{}*
Valor da venda: R$ *{}*
Lucro com a venda: R$ *{}*
Data e horário da venda: *{}*
'''


def create_outflow_message(username, product_name, quantity, total_value, profit_value, timestamp):
    formatted_total_value = number_format(
        total_value,
        force_grouping=True,
        decimal_pos=2,
        use_l10n=True
    )
    formatted_profit_value = number_format(
        profit_value,
        force_grouping=True,
        decimal_pos=2,
        use_l10n=True
    )

    return outflow_message.format(username, product_name, quantity, formatted_total_value, formatted_profit_value, timestamp).strip()
