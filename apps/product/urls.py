from django.urls import path

<<<<<<< HEAD
from apps.product.views import (
    ProductListAPIView, ProductDetailAPIView, LatestAPIView,
    BestsellerAPIView, SortByAPIView
)


urlpatterns = [
    path('products/', ProductListAPIView.as_view(),
         name='product-list'),
    path('product/<slug:slug>/', ProductDetailAPIView.as_view(),
         name='product-detail'),
    path('latest/', LatestAPIView.as_view(),
         name='latest-products'),
    path('bestseller/', BestsellerAPIView.as_view(),
         name='best-seller'),
    path('sort-by/', SortByAPIView.as_view(),
         name='sort-by'),

    # category
    #     path('category/', CategoryListAPIView.as_view(),
    #          name='category-list'),
    #     path('category/<slug:slug>/', CategoryDetailAPIView.as_view(),
    #          name='category-detail')
=======
from apps.product.views import CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), 
        name='category-list'),
    path('category/<slug:slug>/', CategoryDetailAPIView.as_view(), 
        name='category-detail')
>>>>>>> 1d4dc74c7944942684d31b4cf8ae74abd138dbd6
]
