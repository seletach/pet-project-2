from django.urls import path
from API.views import (PostList,
                       PostDetail,
                       UserDetail,
                       UserList,
                       CommentList,
                       CommentDetail,
                       user_post_list,
                       user_comment_list)

app_name = 'api'

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),

    path('users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/<int:pk>/posts/', user_post_list),
    path('user/<int:pk>/comments/', user_comment_list),

    path('comments/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view())
]