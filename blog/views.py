from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from blog.models import Post, Category, Tag, Like, Comment
from blog.read_serializers import PostReadSerializer
from blog.serializers import PostSerializers, CategorySerializer, TagSerializer
from config.pagination import CustomPagePagination


class CategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        category = Category.objects.all().order_by('name')
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, id):
        try:
            category = Category.objects.get(pk = id)
            return category
        except Category.DoesNotExist:
            return None
        
    def get(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error":"Category not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error":"Category not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error":"Category not found."}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({"message": "Category deleted successfully."}, status= status.HTTP_204_NO_CONTENT)


class TagApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        tag = Tag.objects.all().order_by('name')
        serializer = TagSerializer(tag, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
class TagDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
       
    def get_object(self, id):
        try:
            tag = Tag.objects.get(pk = id)
            return tag
        except Tag.DoesNotExist:
            return None
        
    def get(self, request, id):
        tag = self.get_object(id)
        if not tag:
            return Response({"error":"Tag not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, id):
        tag = self.get_object(id)
        if not tag:
            return Response({"error":"Tag not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TagSerializer(tag, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        tag = self.get_object(id)
        if not tag:
            return Response({"error":"Tag not found."}, status=status.HTTP_404_NOT_FOUND)
        tag.delete()
        return Response({"message": "Tag deleted successfully."}, status= status.HTTP_204_NO_CONTENT)


class PostListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        paginator = CustomPagePagination()
        paginated_posts = paginator.paginate_queryset(posts, request)
        serializer = PostReadSerializer(paginated_posts, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)
    
    
    def post(self, request):
        serializer = PostSerializers(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,id):
        try:
            post = Post.objects.get(pk = id)
            return post
        except Post.DoesNotExist:
            return None
        
    def get(self, request, id):
        post = self.get_object(id)
        if not post:
            return Response({"error":"Post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostReadSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, id):
        post = self.get_object(id)
        if not post:
            return Response({"error":"Post not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializers(post, data = request.data, partial = True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        post = self.get_object(id)
        if not post:
            return Response({"error":"Post not found."}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)