from django.urls import path
from .views import (PostsList, PostDetail, PostsCreate, PostsUpdate, PostsDelete, PostsSearch)


urlpatterns = [
    path('posts/', PostsList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostsCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostsUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', PostsDelete.as_view(), name='posts_delete'),
    path('search/', PostsSearch.as_view(), name='posts_search'),

]
