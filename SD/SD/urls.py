"""SD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from users.models import MyUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('posts.urls', namespace='posts')),
    
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', CreateView.as_view( # передать сюда расширенного юзера
        template_name='registration/registration_form.html',
        model=MyUser,
        form_class=UserCreationForm,
        success_url=reverse_lazy('blog:index')),
        name='registration'),
]
