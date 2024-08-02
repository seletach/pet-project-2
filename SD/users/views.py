from django.shortcuts import render, get_object_or_404
from users.models import MyUser
from users.forms import MyUserForm

# Create your views here.

def user_profile(request, user_id):

    # instance = get_object_or_404(MyUser, user_id)
    instance = ''
    form = MyUserForm(request.POST or None)

    # if form.is_valid():
    #     form.save()

    context = {
        'user': MyUser.objects.get(id=user_id),
        'user_form': form
    }
    return render(request, 'users/user_profile.html', context)
