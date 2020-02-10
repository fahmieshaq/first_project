from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'desc', 'author', 'date_created', 'date_modified',)
        read_only_fields = ('date_created', 'date_modified',)
