from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from .models import Good, Category
from .serializers import GoodListSerializer, CategoryListSerializer

client = Client()


class GetAllGoodsTest(TestCase):
    """ Test module for GET all goods API """
    def setUp(self):
        Good.objects.create(name='Phone', slug='phone', price=1234)
        Good.objects.create(name='Microwave', slug='microwave', price=1234)
        Good.objects.create(name='Бокалы', slug='glasses', price=1234)
        Good.objects.create(name='Кофта', slug='sweater', price=1234)

    def test_get_all_goods(self):
        response = client.get(reverse('good-list'))
        goods = Good.objects.all()
        serializer = GoodListSerializer(goods, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_good_by_slug(self):
        response = client.get(reverse('good_slug', kwargs={'slug': 'phone'}))
        good = Good.objects.get(slug='phone')
        serializer = GoodListSerializer(good)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllCategoriesTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Bath', slug='bath')
        Category.objects.create(name='Clothes', slug='clothes')
        Category.objects.create(name='Electronics', slug='electronics')

    def test_get_all_categories(self):
        response = client.get(reverse('category-list'))
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_first_categories(self):
        response = client.get(reverse('category-detail', kwargs={'pk': 1}))
        category = Category.objects.get(pk=1)
        serializer = CategoryListSerializer(category)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_by_slug(self):
        response = client.get(reverse('category_slug', kwargs={'slug':
                                                               'bath'}))
        category = Category.objects.get(slug='bath')
        serializer = CategoryListSerializer(category)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
