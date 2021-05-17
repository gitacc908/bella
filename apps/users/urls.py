from django.urls import path

from apps.users.views import BookmarkAPIListView, BookmarkAPIAddView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('bookmark/', BookmarkAPIListView.as_view(),
         name='user-bookmark'),
    path('bookmark-add/', BookmarkAPIAddView.as_view(),
         name='bookmark-add'),

    # token obtain
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
