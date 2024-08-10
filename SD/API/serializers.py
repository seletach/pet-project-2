from rest_framework import serializers

from posts.models import Post, Comments
from users.models import MyUser

from drf_spectacular.utils import extend_schema, extend_schema_serializer

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'author',
                  'is_published',
                  'title',
                  'text',
                  'image',
                  'category',
                  'comments')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id',
                  'is_superuser',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'bio',
                  'status',
                  'campus',
                  'group',
                  'birth_date',
                  'posts')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = ('id',
                  'is_published',
                  'text',
                  'author',
                  'post')