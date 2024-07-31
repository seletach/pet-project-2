from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # path('login/', auth_views.LoginView(template_name='')),
    # path('', include('django.contrib.auth.urls')),
]