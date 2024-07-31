from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('post_form/', views.post_form, name='post_form')
]
