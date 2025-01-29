from categories.models import Category
from brands.models import Brand
from suppliers.models import Supplier
from products.models import Product
from inflows.models import Inflow
from outflows.models import Outflow
from .data import brands_data, categories_data, suppliers_data, products_data, inflows_data, outflows_data


def run():
    # Clear all data from the database
    Brand.objects.all().delete()
    Category.objects.all().delete()
    Supplier.objects.all().delete()
    Product.objects.all().delete()
    Inflow.objects.all().delete()
    Outflow.objects.all().delete()

    # Create brands in an optimized way (avoiding duplicates)
    brands_to_create = []
    for brand_name, description in brands_data:
        brand, created = Brand.objects.get_or_create(name=brand_name, defaults={'description': description})
        if created:
            brands_to_create.append(brand)

    # Create categories in an optimized way (avoiding duplicates)
    categories_to_create = []
    for name, description in categories_data:
        category, created = Category.objects.get_or_create(name=name, defaults={'description': description})
        if created:
            categories_to_create.append(category)

    # Create suppliers in an optimized way (avoiding duplicates)
    suppliers_to_create = []
    for name, description in suppliers_data:
        supplier, created = Supplier.objects.get_or_create(name=name, defaults={'description': description})
        if created:
            suppliers_to_create.append(supplier)

    # Create products in an optimized way (avoiding duplicates)
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
            print(f"Brand '{brand_name}' not found!")
        except Category.DoesNotExist:
            print(f"Category '{category_name}' not found!")

    Product.objects.bulk_create(products_to_create)

    # Create inflows in an optimized way (avoiding duplicates)
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
            print(f"Supplier '{supplier_name}' not found!")
        except Product.DoesNotExist:
            print(f"Product '{product_title}' not found!")

    Inflow.objects.bulk_create(inflows_to_create)

    # Create outflows in an optimized way (avoiding duplicates)
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
            print(f"Product '{product_title}' not found!")

    Outflow.objects.bulk_create(outflows_to_create)

    print("Database populated successfully!")
