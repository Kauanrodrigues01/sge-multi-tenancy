from categories.models import Category

def run():
    for i in range(1, 101):
        Category.objects.create(name=f'Categoria {i}', description=f'Descrição para Categoria{i}')
