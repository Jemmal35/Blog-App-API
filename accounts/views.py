from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.read_serializer import UserProfileReadSerializer

from .serializers import UserRegistrationSerializer, UserProfileUpdateSerializer, UserPasswordUpdateSerializer
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
    
        
class UserProfileUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request):
        profile = request.user.profile
        serializer = UserProfileUpdateSerializer(profile, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdatePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request):
        serializer = UserPasswordUpdateSerializer(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully."}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # blacklist the refresh token
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)