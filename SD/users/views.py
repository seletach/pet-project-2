from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from users.models import MyUser
from users.forms import MyUserForm


def user_profile(request, username):
    """
    Информация пользователя
    """

    context = {
        'user': MyUser.objects.get(username=username)
    }
    return render(request, 'users/user_profile.html', context)


def user_profile_edit(request, username):
    """
    Форма редактирования данных о пользователе
    """

    instance = get_object_or_404(MyUser, username=username)
    form = MyUserForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/profile/'+ f'{username}/') # переделать хард код
    context = {
        'user_form': form,
    }
    return render(request, 'users/user_profile.html', context)
