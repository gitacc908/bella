from django.urls import path

from apps.category.views import CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<slug:slug>/', CategoryDetailAPIView.as_view(), name='category-detail')
]
