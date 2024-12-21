# scripts/populate_brands.py
from brands.models import Brand

brands_data = [
    ('Nike', 'Marca de roupas e calçados esportivos'),
    ('Adidas', 'Marca de roupas e calçados esportivos'),
    ('Apple', 'Tecnologia, design de produtos eletrônicos e software'),
    ('Samsung', 'Eletrônicos, eletrodomésticos e dispositivos móveis'),
    ('Coca-Cola', 'Refrigerantes e bebidas não alcoólicas'),
    ('Pepsi', 'Refrigerantes e bebidas não alcoólicas'),
    ('Sony', 'Eletrônicos e produtos de entretenimento'),
    ('Microsoft', 'Tecnologia, software e serviços de computação'),
    ('Google', 'Tecnologia, serviços de pesquisa e publicidade digital'),
    ('Amazon', 'Comércio eletrônico e serviços de nuvem'),
    ('Toyota', 'Fabricante de automóveis e produtos de transporte'),
    ('Honda', 'Fabricante de automóveis e motocicletas'),
    ('Boeing', 'Aeronáutica e fabricação de aviões'),
    ('Tesla', 'Automóveis elétricos e energia renovável'),
    ('McDonald\'s', 'Rede de fast food e alimentos'),
    ('Starbucks', 'Cafés e bebidas de café'),
    ('Nike', 'Produtos esportivos e roupas'),
    ('Under Armour', 'Marca de roupas esportivas'),
    ('H&M', 'Moda e roupas acessíveis'),
    ('Zara', 'Moda e vestuário')
]

def run():
    for brand_name, description in brands_data:
        brand = Brand(name=brand_name, description=description)
        brand.save()
