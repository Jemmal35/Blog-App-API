from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import LogoutAPIView, UserRegistrationView, UserProfileView, UserProfileUpdateView, UpdatePasswordView

urlpatterns = [
    path("api/v1/admin/", include('accounts.role_management.urls'), name = 'admin'),
    path("api/v1/register/", UserRegistrationView.as_view(), name= 'registration'),
    path("api/v1/login/",TokenObtainPairView.as_view(), name= 'login'),
    path("api/v1/logout/", LogoutAPIView.as_view(), name="logout"),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name= 'refresh'),
    path("api/v1/profile/", UserProfileView.as_view(), name= 'user-profile'),
    path("api/v1/profile/update/", UserProfileUpdateView.as_view(), name= 'user-profile-update'),
    path("api/v1/profile/change-password/", UpdatePasswordView.as_view(), name='change-password'),
]
