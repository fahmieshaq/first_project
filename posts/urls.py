from django.urls import path
from .views import GetPostList, GetPostDetail, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('posts/', GetPostList.as_view(), name="posts_list"),
    path('posts/add/', CreatePost.as_view(), name="posts_create"),
    path('posts/<int:pk>/', GetPostDetail.as_view(), name="posts_detail"),
    path('posts/edit/<int:pk>/', UpdatePost.as_view(), name="posts_update"),
    path('posts/delete/<int:pk>/', DeletePost.as_view(), name="posts_delete"),
]