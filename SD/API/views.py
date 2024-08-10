from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

from posts.models import Post, Comments
from users.models import MyUser
from API.serializers import (PostSerializer,
                             UserSerializer,
                             CommentSerializer)
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(tags=["Posts"], summary='Получить список постов.')
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema(tags=["Posts"])
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Возвращает, изменяет, удаляет пост"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@extend_schema(tags=["User"])
class UserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
@api_view(['GET'])
def user_post_list(request, pk):
    posts = Post.objects.filter(author_id=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

 
@extend_schema(tags=["User"])
@api_view(['GET'])
def user_comment_list(request, pk):
    comments = Comments.objects.filter(author_id=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@extend_schema(tags=["Comments"])
class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


@extend_schema(tags=["Comments"])
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
