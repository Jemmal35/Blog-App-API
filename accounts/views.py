from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "message": "User registered successfully."}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)