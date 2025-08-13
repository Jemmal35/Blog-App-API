from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path("api/v1/posts/",PostListView.as_view(), name='post-list'),
    path("api/v1/posts/<id>/",PostDetailView.as_view(), name='post-detail')
    
]
