from django.urls import path
from posts import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),

    path('post_write/', views.post_write, name='post_write'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),

    path('post/<int:post_id>/', views.post_card, name='post_card'),

    path('post/<int:post_id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),


]
