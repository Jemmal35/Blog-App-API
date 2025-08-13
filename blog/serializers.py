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
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), required = False, allow_null = True)
    tag = serializers.PrimaryKeyRelatedField(queryset = Tag.objects.all(), required = False, allow_null = True)
    
    class Meta:
        model = Post
        fields = ['title','content','image','status','category','tag']
        
    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(author = user, **validated_data)
        return post
    
    def update(self, instance ,validated_data):
        for atts, value in validated_data.items():
            setattr(instance, atts, value)
        instance.save()
        return instance
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post','content']
        
        def create(self, validated_data):
            user = self.context['request'].user
            comment = Comment.objects.create(user = user, **validated_data)
            return comment
        
        