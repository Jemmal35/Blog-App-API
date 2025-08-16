from django.urls import path
from .views import PostListView, PostDetailView, CategoryApiView, CategoryDetailApiView, TagApiView, TagDetailApiView, CommentApiView, LikeApiView


urlpatterns = [
    path("api/v1/posts/",PostListView.as_view(), name='post-list'),
    path("api/v1/posts/<id>/",PostDetailView.as_view(), name='post-detail'),
    path("api/v1/category/", CategoryApiView.as_view(), name= 'category'),
    path("api/v1/category/<id>/", CategoryDetailApiView.as_view(), name= 'category-detail'),
    path("api/v1/tag/", TagApiView.as_view(), name= 'tag'),
    path("api/v1/tag/<id>/", TagDetailApiView.as_view(), name= 'tag-detail'),
    path("api/v1/posts/<post_id>/comments/", CommentApiView.as_view(), name = 'post-comments'),
    path("api/v1/posts/<post_id>/like/", LikeApiView.as_view(), name = 'like-comments'),
    
]
