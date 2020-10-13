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
from .views import all_posts_view, liked_by_user_view, following_posts_view

app_name = 'Posts'

urlpatterns = [
    path('explore/', all_posts_view, name="all_posts_url"),
    path('liked/', liked_by_user_view, name="liked_by_user_url"),
    path('home/', following_posts_view, name="following_posts_url")
]
