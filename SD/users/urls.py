from django.urls import path
from users import views 


app_name = 'users'

urlpatterns = [
    path('<int:user_id>/', views.user_profile, name='user_profile'), # вместо id использовать username
]