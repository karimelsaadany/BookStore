from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data = Category.objects.create(name='django', slug='django')

    def test_category_model_return(self):
        data = self.data
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data = Product.objects.create(title='django beginners', slug='django-beginners',
                                           price=20, category_id=1, created_by_id=1, image='django')

    def test_product_model_return(self):
        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')
