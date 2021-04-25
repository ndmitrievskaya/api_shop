import json
import os

import django
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from .models import Good
from .serializers import GoodListSerializer

client = Client()


class GetAllGoodsTest(TestCase):
    """ Test module for GET all goods API """

    def setUp(self):
        Good.objects.create(
            name='Phone', slug='phone', price=1234)
        Good.objects.create(
            name='Microwave', slug='microwave', price=1234)
        Good.objects.create(
            name='Бокалы', slug='glasses', price=1234)
        Good.objects.create(
            name='Кофта', slug='sweater', price=1234)

    def test_get_all_goods(self):
        response = client.get(reverse('good-list'))
        goods = Good.objects.all()
        serializer = GoodListSerializer(goods, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
