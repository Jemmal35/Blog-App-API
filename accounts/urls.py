from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView, UserProfileView, UserProfileUpdateView, UpdatePasswordView

urlpatterns = [
    path("api/v1/register/", UserRegistrationView.as_view(), name= 'registration'),
    path("api/v1/login/",TokenObtainPairView.as_view(), name= 'login'),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name= 'refresh'),
    path("api/v1/profile/", UserProfileView.as_view(), name= 'user-profile'),
    path("api/v1/profile/update/", UserProfileUpdateView.as_view(), name= 'user-profile-update'),
    path("api/v1/profile/change-password/", UpdatePasswordView.as_view(), name='change-password'),
]
