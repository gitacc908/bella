from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView

from apps.users.models import Bookmark
from apps.users.serializers import BookmarkSerializer
from rest_framework.response import Response


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


# class UserView(APIView):
#     permission_classes = (permissions.IsAuthenticated, )

#     def get(self, request):
#         return Response('Ok')


# @api_view()
# def userView(request):
#     return Response({"message": "Hello, world!"})
