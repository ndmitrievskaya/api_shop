from rest_framework import serializers
from .models import Good


class GoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"
