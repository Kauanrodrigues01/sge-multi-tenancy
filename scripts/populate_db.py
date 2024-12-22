from categories.models import Category
from brands.models import Brand
from suppliers.models import Supplier
from products.models import Product
from inflows.models import Inflow
from outflows.models import Outflow
from .data import brands_data, categories_data, suppliers_data, products_data, inflows_data, outflows_data

def run():
    # Limpar dados existentes
    Brand.objects.all().delete()
    Category.objects.all().delete()
    Supplier.objects.all().delete()
    Product.objects.all().delete()
    Inflow.objects.all().delete()
    Outflow.objects.all().delete()

    # Criar as marcas de forma otimizada (evitando duplicidade)
    brands_to_create = []
    for brand_name, description in brands_data:
        brand, created = Brand.objects.get_or_create(name=brand_name, defaults={'description': description})
        if created:
            brands_to_create.append(brand)

    # Criar as categorias de forma otimizada (evitando duplicidade)
    categories_to_create = []
    for name, description in categories_data:
        category, created = Category.objects.get_or_create(name=name, defaults={'description': description})
        if created:
            categories_to_create.append(category)

    # Criar os fornecedores de forma otimizada (evitando duplicidade)
    suppliers_to_create = []
    for name, description in suppliers_data:
        supplier, created = Supplier.objects.get_or_create(name=name, defaults={'description': description})
        if created:
            suppliers_to_create.append(supplier)

    # Criar os produtos com bulk_create para otimização
    products_to_create = []
    for title, description, brand_name, category_name, cost_price, selling_price, quantity in products_data:
        try:
            brand = Brand.objects.get(name=brand_name)
            category = Category.objects.get(name=category_name)
            products_to_create.append(Product(
                title=title,
                description=description,
                brand=brand,
                category=category,
                cost_price=cost_price,
                selling_price=selling_price,
                quantity=quantity
            ))
        except Brand.DoesNotExist:
            print(f"Marca '{brand_name}' não encontrada!")
        except Category.DoesNotExist:
            print(f"Categoria '{category_name}' não encontrada!")
    
    Product.objects.bulk_create(products_to_create)

    # Criar as entradas de estoque com bulk_create
    inflows_to_create = []
    for supplier_name, product_title, quantity, description in inflows_data:
        try:
            supplier = Supplier.objects.get(name=supplier_name)
            product = Product.objects.get(title=product_title)
            inflows_to_create.append(Inflow(
                supplier=supplier,
                product=product,
                quantity=quantity,
                description=description
            ))
        except Supplier.DoesNotExist:
            print(f"Fornecedor '{supplier_name}' não encontrado!")
        except Product.DoesNotExist:
            print(f"Produto '{product_title}' não encontrado!")
    
    Inflow.objects.bulk_create(inflows_to_create)

    # Criar as saídas de estoque com bulk_create
    outflows_to_create = []
    for product_title, quantity, description in outflows_data:
        try:
            product = Product.objects.get(title=product_title)
            outflows_to_create.append(Outflow(
                product=product,
                quantity=quantity,
                description=description
            ))
        except Product.DoesNotExist:
            print(f"Produto '{product_title}' não encontrado!")
    
    Outflow.objects.bulk_create(outflows_to_create)

    print("População do banco de dados concluída.")
