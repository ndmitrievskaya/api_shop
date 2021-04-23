from django_filters import RangeFilter
from rest_framework import generics, viewsets, status, filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from .serializers import GoodListSerializer, CategoryListSerializer
from .models import Good, Category


class PriceFilter(FilterSet):
    price = RangeFilter()
    filterset_fields = ['is_published', 'is_deleted']

    class Meta:
        model = Good
        fields = ['price', 'is_published', 'is_deleted']


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = PriceFilter
    search_fields = ['name']
    price = RangeFilter()

    def destroy(self, request, *args, **kwargs) -> Response:
        if kwargs['slug']:
            pass
        good = Good.objects.get(pk=kwargs['pk'])
        good.is_deleted = True
        good.save()
        return Response(status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

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


class ListGoodBySlug(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodListSerializer

    def get_object(self):
        obj = get_object_or_404(Good, slug=self.kwargs['slug'])
        return obj


class ListCategoryBySlug(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryListSerializer

    def get_object(self):
        obj = get_object_or_404(Category, slug=self.kwargs['slug'])
        return obj
