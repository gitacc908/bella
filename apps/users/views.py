from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from apps.product.models import Product
from apps.users.serializers import (
    UserBookmarkSerializer, UserSerializer, RegisterSerializer
)


User = get_user_model()


class UserAPICreateView(generics.CreateAPIView):
    queryset = User
    serializer_class = RegisterSerializer


class UserAPIListView(generics.ListAPIView):
    queryset = User
    serializer_class = UserSerializer


class BlackListTokenView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BookmarkAPIDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBookmarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return generics.get_object_or_404(User, phone=self.request.user.phone)


class AddToBookmarkView(generics.UpdateAPIView):
    """
        API geting product ID to add this product into user's bookmark
    """
    queryset = User.objects.all()
    serializer_class = UserBookmarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return generics.get_object_or_404(User, phone=self.request.user.phone)

    def perform_update(self, serializer):
        user_bookmark = self.get_object()
        try:
            user_bookmark.favorite_products.add(
                serializer.validated_data.get('favorite_products')[0]
            )
        except IndexError:
            return Response('Index out of range')


class DeleteFromBookmarkView(generics.UpdateAPIView):
    """
        API geting product ID to delete this product from user's bookmark
    """
    queryset = User.objects.all()
    serializer_class = UserBookmarkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return generics.get_object_or_404(User, phone=self.request.user.phone)

    def perform_update(self, serializer):
        try:
            product = serializer.validated_data.get('favorite_products')[0]
        except IndexError:
            Response('Index out of range')
        else:
            user_bookmark = self.get_object()
            user_bookmark.favorite_products.remove(product)
