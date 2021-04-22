from rest_framework import generics, viewsets

from .serializers import GoodDetailSerializer, GoodListSerializer, \
    CategoryDetailSerializer, CategoryListSerializer
from .models import Good, Category


class GoodCreateView(generics.CreateAPIView):
    serializer_class = GoodDetailSerializer


class GoodViewSet(viewsets.ModelViewSet):
    serializer_class = GoodListSerializer

    def get_queryset(self):
        goods = Good.objects.all()
        return goods


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories
