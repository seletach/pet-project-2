from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

MyUser = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2')
        field_classes = {'username': UsernameField}


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name',
                   'last_name',
                   'email',
                   'bio',
                   'status',
                   'campus',
                   'group',
                   'birth_date')
