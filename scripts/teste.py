from products.models import Product
from inflows.models import Inflow
from suppliers.models import Supplier
from categories.models import Category
from brands.models import Brand
from django.contrib.auth.models import User


def run():
    # Criando um usuário (se não houver)
    user, _ = User.objects.get_or_create(username='testuser')

    # Criando um fornecedor (se não houver)
    supplier, _ = Supplier.objects.get_or_create(name='Fornecedor Teste', user=user, description='Testando')

    # Criando uma categoria (se não houver)
    categoria, _ = Category.objects.get_or_create(name='Categoria Teste', user=user, description='Testando')

    # Criando uma marca (se não houver)
    marca, _ = Brand.objects.get_or_create(name='Marca teste', user=user, description='Testando')

    # Criando um produto (se não houver)
    product, _ = Product.objects.get_or_create(
        user=user,
        title='Produto Teste',
        cost_price=10.00,
        selling_price=20.00,
        category=categoria,
        brand=marca
    )

    # Criando algumas entradas de estoque (Inflow)
    Inflow.objects.create(user=user, supplier=supplier, product=product, quantity=5, cost_price=10.00, selling_price=20.00)
    Inflow.objects.create(user=user, supplier=supplier, product=product, quantity=10, cost_price=10.00, selling_price=20.00)
    Inflow.objects.create(user=user, supplier=supplier, product=product, quantity=3, cost_price=10.00, selling_price=20.00)

    # Testando a propriedade quantity do produto
    print(f"Quantidade total em estoque do produto '{product.title}': {product.quantity}")
