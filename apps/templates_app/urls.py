from django.urls import path

from apps.templates_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
]
