"""
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        pass
"""
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, permissions
from .permissions import IsAuthorOrSuperuser


class GetPostList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetPostDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(generics.UpdateAPIView):
    permission_classes = (IsAuthorOrSuperuser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrSuperuser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
