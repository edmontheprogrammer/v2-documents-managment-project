# Note 1: imprting " login, authenticate" and "UserCreationForm"
# to create the user registeration form from Django.
# "UserCreationForm" is a built-in form from Django that allows us to create
# users and user accounts in Django
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Note 2: "from django import forms" is used to gain access to the
# built-in "forms" fields which gives us access to additional attributes
# that can be added as additional information to the "User" object
from django import forms

# Getting access to the "Django's built-in" model
from django.contrib.auth.models import User


class CustomUserObjectForm(UserCreationForm):
    # Note 3: By default, "User" object has "email", "first_name",
    # "last_name", "username", "password1" and "password2" as built-in fileds
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    # This line defines "AdditionalAttributesToUserObjectForm" to be saved in the
    # "User"'s database that comes built-in with Django
    class Meta:
        model = User
        # Note 4: The Additional "fields" that appears on the form UI for the
        # user when creating new account
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]


# Note 5: This "CustomUserObjectForm" will now replace or overwrite the
# "built-in UserCreationForm" that comes with Django
