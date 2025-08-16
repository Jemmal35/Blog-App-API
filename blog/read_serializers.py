from rest_framework import serializers

from blog.models import Comment, Post
from blog.serializers import AuthorSerializer, CategorySerializer, TagSerializer

class CommentReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at"]
        

class PostReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    category = CategorySerializer(read_only = True)
    tags = TagSerializer(many = True,read_only = True)
    likes_count = serializers.IntegerField(source = "likes.count", read_only = True)
    comments = CommentReadSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'slug', 'content', 'image', 'status',
            'category', 'tags', 'likes_count', 'comments_count', 'comments',
            'created_at', 'updated_at'
        ]
    
    def get_comments_count(self, obj):
        return obj.comments.count()