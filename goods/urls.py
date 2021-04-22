from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from goods.views import GoodCreateView, GoodViewSet, CategoryCreateView, \
    CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register(r"goods", GoodViewSet, basename="good")
router_v1.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("v1/goods/create/", GoodCreateView.as_view()),
    path("v1/categories/create/", CategoryCreateView.as_view()),
    path('v1/', include(router_v1.urls)),
]
