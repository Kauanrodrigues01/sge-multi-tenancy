from suppliers.models import Supplier

def run():
    for i in range(1, 101):
        Supplier.objects.create(name=f'Categoria {i}', description=f'Descrição para Categoria{i}')
