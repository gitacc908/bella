from django.urls import path

from apps.users.views import (
    BookmarkAPIDetailView, AddToBookmarkView,
    DeleteFromBookmarkView, UserAPICreateView,
)

urlpatterns = [
    path('sign-up/', UserAPICreateView.as_view(),
         name='sign-up'),
    path('bookmark/', BookmarkAPIDetailView.as_view(),
         name='user-bookmark'),
    path('bookmark-add/', AddToBookmarkView.as_view(),
         name='bookmark-add'),
    path('bookmark-delete/', DeleteFromBookmarkView.as_view(),
         name='bookmark-delete')
]
