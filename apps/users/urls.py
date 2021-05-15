from django.urls import path

from apps.users.views import BookmarkAPIListView, BookmarkAPIAddView

urlpatterns = [
    path('bookmark/', BookmarkAPIListView.as_view(), name='user-bookmark'),
    path('bookmark-add/', BookmarkAPIAddView.as_view(), name='bookmark-add')
]
