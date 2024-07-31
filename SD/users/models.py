from django.db import models
from django.contrib.auth.models import AbstractUser


MAX_LENGHT = 100


class MyUser(AbstractUser):
    """Расширенный профиль."""
    bio = models.TextField('Биография', blank=True)
    status = models.CharField(max_length=MAX_LENGHT, blank=True)
    campus = models.CharField(
        max_length=MAX_LENGHT,
        help_text='Колледж/ Институт')
    group = models.CharField(
        max_length=MAX_LENGHT,
        blank=True,
        help_text='Группа, например: ТД-22-3')
    birth_date = models.DateField(null=True, blank=True)


class Roles_for_MyUser(models.Model):
    """Роли для пользователей."""
    title = models.CharField(max_length=MAX_LENGHT)
    profile = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='roles')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title
