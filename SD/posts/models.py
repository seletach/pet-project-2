from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


user = get_user_model()
MAX_LENGHT = 100


class BaseModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовать')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Категория добавлена')

    class Meta:
        abstract = True


class Category(BaseModel):
    """Категории для постов."""
    title = models.CharField(max_length=MAX_LENGHT)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(BaseModel):
    """Пост."""
    title = models.CharField(max_length=MAX_LENGHT)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,
                               on_delete=models.CASCADE,
                               related_name='posts')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)
    image = models.ImageField(null=True,upload_to='post_images')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Comments(BaseModel):
    """Комментарии для постов."""
    text = models.TextField()
    author = models.ForeignKey(user,
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')

    class Meta:
        ordering = ('created_at',)


class Tags_for_Post(models.Model):
    """Тэги для постов."""
    title = models.CharField(max_length=MAX_LENGHT)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='tags')
