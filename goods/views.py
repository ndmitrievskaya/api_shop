from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from .serializers import GoodListSerializer, CategoryListSerializer
from .models import Good, Category


class GoodViewSet(viewsets.ModelViewSet):
    serializer_class = GoodListSerializer

    def get_queryset(self):
        goods = Good.objects.all()
        return goods

    def destroy(self, request, *args, **kwargs) -> Response:
        good = Good.objects.get(pk=kwargs['pk'])
        good.is_deleted = True
        good.save()
        return Response(status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        categories = Category.objects.all()
        return categories

    def destroy(self, request, *args, **kwargs):
        if not list(Good.objects.filter(category=kwargs['pk'])):
            category = Category.objects.get(pk=kwargs['pk'])
            return super(Category, category).destroy(*args, **kwargs)
        return Response(
            "Deleting error: You can't delete this category as it's connected with existing goods",
            status=status.HTTP_403_FORBIDDEN)
