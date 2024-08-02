from django.urls import path
from posts import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_form/', views.post_form, name='post_form'),
    path('post_card/<int:id>/', views.post_card, name='post_card')
]
