from django.urls import path
from .views import PostListView, PostDetailView, CategoryApiView, CategoryDetailApiView, TagApiView, TagDetailApiView


urlpatterns = [
    path("api/v1/posts/",PostListView.as_view(), name='post-list'),
    path("api/v1/posts/<id>/",PostDetailView.as_view(), name='post-detail'),
    path("api/v1/category/", CategoryApiView.as_view(), name= 'category'),
    path("api/v1/category/<id>/", CategoryApiView.as_view(), name= 'category-detail'),
    path("api/v1/tag/", CategoryApiView.as_view(), name= 'tag'),
    path("api/v1/tag/<id>/", CategoryApiView.as_view(), name= 'tag-detail'),   
    
]
