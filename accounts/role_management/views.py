from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from accounts.models import User
from .serializers import UserRoleUpdateSerializer

class UserRoleUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]  # only Django admin users can access

    def put(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRoleUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": f"Role updated to {serializer.data['role']}"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
