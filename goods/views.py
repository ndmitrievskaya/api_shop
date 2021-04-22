from rest_framework import generics
from .serializers import GoodDetailSerializer


class GoodCreateView(generics.CreateAPIView):
    serializer_class = GoodDetailSerializer
