from django.urls import path
from apps.product.views import CategoryListAPIView, CategoryDetailAPIView

from apps.product.views import (
    ProductListAPIView, ProductDetailAPIView, LatestAPIView,
    BestsellerAPIView, SortByAPIView, SearchAPIView
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
    path('search_products/', SearchAPIView.as_view(),
         name='search_products'),

    # category
    path('category/', CategoryListAPIView.as_view(),
         name='category-list'),
    path('category/<slug:slug>/', CategoryDetailAPIView.as_view(),
         name='category-detail')
]
