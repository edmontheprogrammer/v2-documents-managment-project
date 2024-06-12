from django.shortcuts import render, redirect

# Note 1: imprting " login, authenticate" and "UserCreationForm"
# to create the user registeration form from Django.
# "UserCreationForm" is a built-in form from Django that allows us to create
# users and user accounts in Django
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

# Note 2:
# This  built-in Django "UserCreationForm" gets replace by "CustomUserObjectForm"
# that we created in "forms.py" file
# from django.contrib.auth.forms import UserCreationForm
#
# Note 3:
from .forms import CustomUserObjectForm

# Create your views here.
#
# Note 1: "request.user":
# "request.user" is a function call that gives us access to the "User" object in
# code ... if you have to modify and get access to the user attributes
# programmatically.


def users(request):
    if request.method == "POST":
        user_form = CustomUserObjectForm(request.POST)
        if user_form.is_valid():
            # This line simply saves the "new user" that we created
            # into the Django's built-in "Users" database or into the Django's
            # system like any other user that you'll create using the
            # " python manage.py createsuperuser " command or creating users
            # in Django from the "admin site"
            user_form.save()
        # redirect the new user to this page ... on successful login
        return redirect("/home")
    else:
        user_form = CustomUserObjectForm()
    return render(request, 'users/users_home.html', {"user_form": user_form})


# Note 2:
# The login_required decorator limits access to logged in users.
@login_required
def profile(request):
    return render(request, 'users/profile.html')
