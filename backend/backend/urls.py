"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include


from users import views as users_app_views

urlpatterns = [

    # the URLs for "login", "logout" for Django's
    #  "django.contrib.auth", app that comes with Django
    # Note 1: Create the HTML pages (HTML templates) for the
    # "login" and "logout" pages in the "users" app and then add the
    # "login" and "logout" authentication logics in these pages to accept
    # user's credentials into the site.
    # Note 2: Make sure the URLs for the "login", "logout" templates are
    # within a directory called "registration". "registration" is a special
    # folder that django looks for when trying to find
    # the  HTML pages (HTML templates) for the "login" and "logout" pages.
    path("accounts/", include("django.contrib.auth.urls")),

    path("admin/", admin.site.urls),



    # This is the URL for the "website" app.
    # It show the home page for the entire django project which is the website app
    path("", include("website.urls"), name="home"),


    # This is the URL for the "users" app.
    # It shows the home page for the "users" app
    path("users/", users_app_views.users, name="users"),


    # This is a URL for the django debug_toolbar app
    path("__debug__/", include("debug_toolbar.urls")),

    # Note 1: The "portal" app has all of the documents the user needs to create 
    # This is where you'll add different forms for the users once they create new 
    # accounts.


]
