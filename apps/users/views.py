from rest_framework import generics
from rest_framework import permissions

from apps.users.models import Bookmark
from apps.users.serializers import BookmarkSerializer


class BookmarkAPIListView(generics.ListAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class BookmarkAPIAddView(generics.UpdateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_object(self):
        return Bookmark.objects.filter(user=self.request.user)[0]
