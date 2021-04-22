from rest_framework import serializers
from .models import Good, Category


class GoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ("id", "name", "category", "price")


class GoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ("id", "name", "category", "price", "is_published", "is_deleted")


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
