from django.urls import path
from . import views

from .views import profile

urlpatterns = [

    path('', views.users, name='users-home'),
    path('profile/', profile, name='users-profile'),
]
