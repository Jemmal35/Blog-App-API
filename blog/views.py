from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from blog.models import Post
from blog.read_serializers import PostReadSerializer
from blog.serializers import PostSerializers
from config.pagination import CustomPagePagination

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
    def get(self, request, id):
        try:
            post = Post.objects.get(pk = id)
        except Post.DoesNotExist:
            return Response({"error":"Post does not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostReadSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, id):
        try:
            post = Post.objects.get(pk = id)
        except Post.DoesNotExist:
            return Response({"error":"Post does not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializers(post, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            post = Post.objects.get(pk = id)
        except Post.DoesNotExist:
            return Response({"error":"Post does not found."}, status=status.HTTP_404_NOT_FOUND)
        
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)