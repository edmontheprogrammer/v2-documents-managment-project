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
    # This is the URL for the "website" app
    path("", include("website.urls")),

    # This is the URL for the "users" app
    path("users/", users_app_views.users, name="users"),

    path("admin/", admin.site.urls),

    # This is a URL for the django debug_toolbar app
    path("__debug__/", include("debug_toolbar.urls")),









]
