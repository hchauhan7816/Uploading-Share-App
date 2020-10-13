"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import update_person_view, register_user_view, login_person_view, home_page_view, logout_person_view
from .views import other_profile_view, follow_person_view

app_name = 'Profile'

urlpatterns = [
    path('register/', register_user_view, name="register_url"),
    path('update/', update_person_view, name="update_url"),
    path('login/', login_person_view, name="login_url"),
    path('logout/', logout_person_view, name="logout_url"),
    path('myprofile', home_page_view, name="myprofile_url"),
    path('others_profile', other_profile_view, name="other_profile_url"),
    path('follow', follow_person_view, name="follow_url"),
]
