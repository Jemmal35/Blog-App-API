from django.urls import path
from .views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/v1/register/", UserRegistrationView.as_view(), name= 'registration'),
    path("api/v1/login/",TokenObtainPairView.as_view(), name= 'login'),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name= 'refresh'),    
]
