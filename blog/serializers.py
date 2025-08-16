from rest_framework import serializers
from .models import Tag, Category, Post, Comment, Like

from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]
        


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class PostSerializers(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        many=True,
        write_only=True
    )
    
    class Meta:
        model = Post
        fields = ['title','content','image','status','category_id','tag_ids']
        
    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        category = validated_data.pop("category", None)
        user = self.context['request'].user
        
        post = Post.objects.create(author=user, category=category, **validated_data)
        if tags:
            post.tags.set(tags)
        return post
    
    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        category = validated_data.pop("category", None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if category:
            instance.category = category
        instance.save()
        
        if tags is not None:
            instance.tags.set(tags)
        
        return instance

    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at']
        

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','user', 'post', 'created_at']
        