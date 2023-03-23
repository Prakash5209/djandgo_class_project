from django.urls import path
from post.views import home,create_post,edit_post,delete_post,comment_post,like_post

app_name = 'post'
urlpatterns = [
    path('',home,name='home'),
    path('create-post/',create_post,name="create_post"),
    path('edit-post/<int:postid>/',edit_post,name="edit_post"),
    path('delete-post/',delete_post,name='delete_post'),
    path('like-post/<int:postid>/',like_post,name="like_post"),
    path('comment-post/<int:postid>/',comment_post,name="comment_post"),
]