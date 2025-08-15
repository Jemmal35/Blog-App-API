from rest_framework import serializers

from .models import User, UserProfile

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "phone_number"]


class UserProfileReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only = True)
    class Meta:
        model = UserProfile
        fields = ["user", "bio","location", "birth_date", "profile_picture"]
        