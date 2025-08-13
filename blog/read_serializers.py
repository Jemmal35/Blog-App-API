from rest_framework import serializers

from blog.models import Comment, Post
from blog.serializers import AuthorSerializer, CategorySerializer, TagSerializer

class CommentReadSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at"]
        

class PostReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    category = CategorySerializer(read_only = True)
    tag = TagSerializer(read_only = True)
    likes_count = serializers.IntegerField(source = "likes.count", read_only = True)
    comments_count = CommentReadSerializer(many = True, read_only = True, source = "comment_set")
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'slug', 'content', 'image','status','category','tag','likes_count', 'comments_count', 'created_at', 'updated_at']
        