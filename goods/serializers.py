from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Good, Category


class GoodListSerializer(serializers.ModelSerializer):

    def validate_category(self, category):
        if len(category) < 2 or len(category) > 10:
            raise serializers.ValidationError(
                "You should choose from 2 to 10 categories to add a good")
        return category

    class Meta:
        model = Good
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
