from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from blog.models import Post
from blog.read_serializers import PostReadSerializer
from blog.serializers import PostSerializers


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostReadSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializers(data = request.data)
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