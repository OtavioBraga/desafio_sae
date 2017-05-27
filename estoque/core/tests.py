from django.core.urlresolvers import reverse
from django.test import RequestFactory
from django.test import TestCase

from unittest.mock import patch, MagicMock

import factory

from .views import ListPurchasesView, NewProductView, NewPurchaseView
from users.models import User
from .models import Product, Purchase


class UserFactory(factory.Factory):
    '''
        Fake user for loginrequired views
    '''
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'


class ProductModelCreateTestCase(TestCase):
    '''
        Test for product create
    '''
    def setUp(self):
        self.id = Product.objects.create(name="queijo").id

    def test_if_product_was_created(self):
        product = Product.objects.filter(id=self.id).exists()
        self.assertTrue(product)


class ProductCreateViewTestCase(TestCase):
    '''
        Test for product create view
        This test case test get(200) and create(302)
        It also asserts that the view call the database only one time when 
        saving a new product.
    '''
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('new-product'))
        request.user = self.user
        response = ListPurchasesView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @patch('core.models.Product.save', MagicMock(name="save"))
    def test_post(self):
        data = {
            'name': 'queijo',
        }
        request = self.factory.post(reverse('new-product'), data)
        request.user = self.user
        response = NewProductView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.save.called)
        self.assertEqual(Product.save.call_count, 1)


class ProductsListViewTest(TestCase):
    '''
        Test for products list
        This test case test get(200)
    '''
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('products-list'))
        request.user = self.user
        response = ListPurchasesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PurchasesListViewTest(TestCase):
    '''
        Test for purchases list
        This test case test get(200)
    '''
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('purchases-list'))
        request.user = self.user
        response = ListPurchasesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PurchaseCreateViewTestCase(TestCase):
    '''
        Test for purchase create view
        This test case test get(200) and create(302)
        It also asserts that the view call the database only one time when 
        saving a new purchase.
    '''
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.product_id = Product.objects.create(name="queijo").id

    def test_get(self):
        request = self.factory.get(reverse('new-purchase'))
        request.user = self.user
        response = NewPurchaseView.as_view()(request, pk=0)
        self.assertEqual(response.status_code, 200)

    @patch('core.models.Purchase.save', MagicMock(name="save"))
    def test_post(self):
        data = {
            'product': self.product_id,
            'quantity': '300',
            'value': '895',
            'purchase_date': '27/05/2017'
        }
        request = self.factory.post(reverse('new-purchase'), data)
        request.user = self.user
        response = NewPurchaseView.as_view()(request, pk=0)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Purchase.save.called)
        self.assertEqual(Purchase.save.call_count, 1)
