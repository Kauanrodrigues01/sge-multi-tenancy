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

categories_data = [
    ('Roupas Esportivas', 'Produtos relacionados ao vestuário esportivo'),
    ('Tecnologia', 'Produtos eletrônicos e acessórios tecnológicos'),
    ('Alimentos e Bebidas', 'Alimentos e bebidas como refrigerantes, cafés, fast food'),
    ('Automóveis', 'Veículos e acessórios automotivos'),
    ('Eletrodomésticos', 'Produtos eletrônicos e eletrodomésticos para uso doméstico'),
    ('Moda', 'Roupas e acessórios de moda'),
    ('Vestuário', 'Produtos relacionados ao vestuário geral'),
    ('Aeronáutica', 'Produtos e serviços relacionados à indústria aeronáutica'),
    ('Energia', 'Produtos relacionados à energia renovável e sustentável'),
]


suppliers_data = [
    ('Nike Inc.', 'Fornecedor de roupas e calçados esportivos'),
    ('Adidas AG', 'Fornecedor de roupas e calçados esportivos'),
    ('Apple Inc.', 'Fornecedor de eletrônicos e tecnologia de consumo'),
    ('Samsung Electronics', 'Fornecedor de eletrônicos e eletrodomésticos'),
    ('Coca-Cola Company', 'Fornecedor de bebidas não alcoólicas e refrigerantes'),
    ('PepsiCo', 'Fornecedor de bebidas e alimentos'),
    ('Sony Corporation', 'Fornecedor de eletrônicos e produtos de entretenimento'),
    ('Microsoft Corporation', 'Fornecedor de software, tecnologia e computação em nuvem'),
    ('Amazon.com', 'Fornecedor de e-commerce e serviços de nuvem'),
    ('Toyota Motors', 'Fornecedor de veículos e automóveis'),
    ('Boeing', 'Fornecedor de produtos aeronáuticos e aviões'),
    ('Tesla, Inc.', 'Fornecedor de automóveis elétricos e soluções de energia renovável'),
]


products_data = [
    ('Camiseta Nike', 'Camiseta esportiva da Nike', 'Nike', 'Roupas Esportivas', 99.99, 150.00, 200),
    ('Tênis Adidas', 'Tênis esportivo da Adidas', 'Adidas', 'Roupas Esportivas', 199.99, 350.00, 50),
    ('iPhone 14', 'Smartphone Apple iPhone 14', 'Apple', 'Tecnologia', 1200.00, 1800.00, 100),
    ('Galaxy S21', 'Smartphone Samsung Galaxy S21', 'Samsung', 'Tecnologia', 999.99, 1500.00, 80),
    ('Coca-Cola Lata', 'Refrigerante Coca-Cola Lata 350ml', 'Coca-Cola', 'Alimentos e Bebidas', 2.50, 5.00, 1000),
    ('Pepsi Lata', 'Refrigerante Pepsi Lata 350ml', 'Pepsi', 'Alimentos e Bebidas', 2.50, 5.00, 1000),
    ('Café Starbucks', 'Café Starbucks grão', 'Starbucks', 'Alimentos e Bebidas', 50.00, 100.00, 300),
    ('Honda Civic', 'Automóvel Honda Civic 2024', 'Honda', 'Automóveis', 25000.00, 35000.00, 10),
    ('Corolla', 'Automóvel Toyota Corolla 2024', 'Toyota', 'Automóveis', 23000.00, 33000.00, 15),
    ('Tesla Model 3', 'Automóvel elétrico Tesla Model 3', 'Tesla', 'Automóveis', 35000.00, 50000.00, 5),
    ('Boing 787', 'Avião Boing 787', 'Boeing', 'Aeronáutica', 120000000.00, 150000000.00, 2),
]


inflows_data = [
    ('Nike Inc.', 'Camiseta Nike', 100, 'Chegada de novas camisetas Nike para estoque'),
    ('Adidas AG', 'Tênis Adidas', 50, 'Entrada de novos tênis Adidas para reposição'),
    ('Apple Inc.', 'iPhone 14', 80, 'Recebimento de novos iPhones 14 da Apple'),
    ('Samsung Electronics', 'Galaxy S21', 60, 'Chegada de Galaxy S21 para estoque'),
    ('Coca-Cola Company', 'Coca-Cola Lata', 500, 'Reposição de latas de Coca-Cola'),
    ('PepsiCo', 'Pepsi Lata', 500, 'Entrada de Pepsi Lata para o estoque'),
    ('Starbucks', 'Café Starbucks', 200, 'Recebimento de novos grãos de café Starbucks'),
    ('Toyota Motors', 'Corolla', 15, 'Entrada de novos Corollas para venda'),
    ('Tesla, Inc.', 'Tesla Model 3', 5, 'Entrada de Tesla Model 3 para o estoque'),
    ('Boeing', 'Boing 787', 1, 'Avião Boeing 787 adquirido'),
]


outflows_data = [
    ('Camiseta Nike', 50, 'Venda de camisetas Nike para clientes'),
    ('Tênis Adidas', 30, 'Venda de tênis Adidas para clientes'),
    ('iPhone 14', 20, 'Venda de iPhones 14 para clientes'),
    ('Galaxy S21', 15, 'Venda de Galaxy S21 para clientes'),
    ('Coca-Cola Lata', 400, 'Venda de Coca-Cola para clientes em lojas'),
    ('Pepsi Lata', 400, 'Venda de Pepsi para clientes em lojas'),
    ('Café Starbucks', 150, 'Venda de grãos de café Starbucks para consumidores'),
    ('Honda Civic', 10, 'Venda de Honda Civic 2024'),
    ('Corolla', 10, 'Venda de Toyota Corolla 2024'),
    ('Tesla Model 3', 3, 'Venda de carros Tesla Model 3'),
    ('Boing 787', 1, 'Venda de aeronave Boeing 787'),
]
