from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer
from .permissions import IsAuthorOrSuperuser


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrSuperuser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
