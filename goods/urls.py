from rest_framework.routers import DefaultRouter
from django.urls import path, include

from goods.views import GoodViewSet, CategoryViewSet, ListGoodBySlug, \
    ListCategoryBySlug

router_v1 = DefaultRouter()
router_v1.register(r"goods", GoodViewSet, basename="good")
router_v1.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [path('v1/', include(router_v1.urls)), ]

urlpatterns += [
    path('v1/goods/slug/<slug:slug>/', ListGoodBySlug.as_view(),
         name='good_slug'),
    path('v1/categories/slug/<slug:slug>/', ListCategoryBySlug.as_view(),
         name='category_slug'),
]
