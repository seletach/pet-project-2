from django.urls import path
from users import views 
from django.contrib.auth.decorators import login_required


app_name = 'users'

urlpatterns = [
    path('<slug:username>/edit/', views.user_profile_edit, name='user_profile_edit'),
    path('<slug:username>/', login_required(views.user_profile), name='user_profile'), # LOGIN_URL
]