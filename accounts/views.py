from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from accounts.read_serializer import UserProfileReadSerializer

from .serializers import UserRegistrationSerializer
from.models import UserProfile

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "message": "User registered successfully."}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        profile = UserProfile.objects.get(user = request.user)
        serializer = UserProfileReadSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        