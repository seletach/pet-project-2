from django.urls import path
from posts import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('post_create/', views.post_create, name='post_create'),

    path('post/<int:post_id>/', views.post_card, name='post_card'),
    path('post/<int:post_id>/edit/', views.post_update, name='post_update'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),

    path('post/<int:post_id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', views.comment_edit, name='comment_edit'),
]
