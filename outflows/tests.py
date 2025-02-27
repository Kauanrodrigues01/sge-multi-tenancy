from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from brands.models import Brand
from categories.models import Category
from suppliers.models import Supplier
from products.models import Product
from inflows.models import Inflow
from outflows.models import Outflow


class OutflowSignalTest(TestCase):

    def setUp(self):
        # Criando usuário
        self.user = User.objects.create_user(username='testuser', password='password')

        # Criando marca
        self.brand = Brand.objects.create(name='Test Brand', description='Test Brand Description', user=self.user)

        # Criando categoria
        self.category = Category.objects.create(name='Test Category', description='Test Category Description', user=self.user)

        # Criando fornecedor
        self.supplier = Supplier.objects.create(name='Test Supplier', description='Test Supplier Description', user=self.user)

        # Criando produto
        self.product = Product.objects.create(
            title='Test Product',
            user=self.user,
            brand=self.brand,
            category=self.category,
            description='Test Product Description',
            serie_number='12345',
            cost_price=10.00,
            selling_price=20.00
        )

        self.now = timezone.now()

        # Criando inflow (entrada de produto)
        self.inflow1 = Inflow.objects.create(
            user=self.user,
            supplier=self.supplier,
            product=self.product,
            quantity=30,
            description='Test Inflow',
        )

        self.inflow1.created_at = (self.now - timedelta(days=1))
        self.inflow1.save()

        self.inflow2 = Inflow.objects.create(
            user=self.user,
            supplier=self.supplier,
            product=self.product,
            quantity=70,
            description='Test Inflow',
            created_at=self.now
        )

    def test_outflow_signal_updates_inflow_quantity(self):
        # Criando um Outflow (saída de produto)
        Outflow.objects.create(
            user=self.user,
            product=self.product,
            quantity=50,  # Estamos retirando 50 do estoque
            description='Test Outflow'
        )

        # A quantidade do Inflow deve ter diminuído de 100 para 50
        self.assertEqual(self.product.quantity, 50)

    def test_outflow_signal_does_not_negative_quantity(self):
        # Criando um Outflow com quantidade maior que o inflow
        Outflow.objects.create(
            user=self.user,
            product=self.product,
            quantity=150,  # Tentando retirar 150, mas só há 100
            description='Test Outflow'
        )

        self.assertIsNone(Outflow.objects.first())
        self.assertEqual(self.product.quantity, 100)  # Não é para acontecer nada já que está tentando vender/tirar mais produtos do que tem

    def test_outflow_signal_multiple_inflows(self):
        # Criando mais inflows
        inflow = Inflow.objects.create(
            user=self.user,
            supplier=self.supplier,
            product=self.product,
            quantity=250,
            description='Second Test Inflow'
        )
        inflow.created_at = (self.now - timedelta(days=2))  # Pagamento mais antigo
        inflow.save()

        # Criando um Outflow de 250 (somando com o anterior)
        Outflow.objects.create(
            user=self.user,
            product=self.product,
            quantity=250,  # Tentando retirar 250
            description='Test Outflow'
        )

        # Verificando as quantidades dos inflows
        inflows = Inflow.objects.filter(product=self.product, user=self.user).order_by('created_at')
        inflows[0].refresh_from_db()  # Primeiro inflow
        inflows[1].refresh_from_db()  # Segundo inflow
        inflows[2].refresh_from_db()  # Terceiro inflows

        self.assertEqual(inflows[0].quantity, 0)  # O primeiro inflow foi esgotado
        self.assertEqual(inflows[1].quantity, 30)  # O segundo inflow ficou com 30
        self.assertEqual(inflows[2].quantity, 70)  # O segundo inflow ficou com 30
        self.assertEqual(self.product.quantity, 100)
