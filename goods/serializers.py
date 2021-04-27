from rest_framework import serializers

from .models import Good, Category


class GoodListSerializer(serializers.ModelSerializer):
    def validate_categories(self, categories) -> Good.categories:
        if len(categories) < 2 or len(categories) > 10:
            raise serializers.ValidationError(
                "You should choose from 2 to 10 categories to add a good")
        return categories

    class Meta:
        model = Good
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
