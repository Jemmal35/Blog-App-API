from django.urls import path
from .views import UserRoleUpdateView

urlpatterns = [
    path('users/<user_id>/role/', UserRoleUpdateView.as_view(), name='update-user-role'),
]
