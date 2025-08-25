from rest_framework import serializers
from accounts.models import User

class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role']

    def validate_role(self, value):
        allowed_roles = ['admin', 'manager', 'user']
        if value not in allowed_roles:
            raise serializers.ValidationError("Invalid role.")
        return value
