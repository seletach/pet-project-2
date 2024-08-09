from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

from posts.models import Post, Comments
from users.models import MyUser
from API.serializers import (PostSerializer,
                             UserSerializer,
                             CommentSerializer)


# @api_view(['GET', 'POST'])
# def post_list(request):
#     """
#     Получение списка всех постов и создание поста.
#     """
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH ', 'DELETE'])
# def post_detail(request, post_id):
#     """
#     Возвращает, редактирует, удаляет пост.
#     """
#     post = Post.objects.get(id=post_id)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def user_post_list(request, pk):
    posts = Post.objects.filter(author_id=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
        

@api_view(['GET'])
def user_comment_list(request, pk):
    comments = Comments.objects.filter(author_id=pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    