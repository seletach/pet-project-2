from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2')
        field_classes = {'username': UsernameField}