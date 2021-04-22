from django.urls import path

from .views import Goods, GoodDetail

urlpatterns = [
    path('', Goods.as_view()),
    path('<int:pk>/', GoodDetail.as_view()),
]