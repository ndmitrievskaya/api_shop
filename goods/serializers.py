from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Good, Category


class GoodListSerializer(serializers.ModelSerializer):
    # category = SerializerMethodField('get_limited_number_of_categories')
    #
    # def get_limited_number_of_categories(self, obj):
    #     qs = obj.category.all()
    #     if len(qs) > 10:
    #         return ValueError

    class Meta:
        model = Good
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
