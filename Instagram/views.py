from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def go_login(request):
    return redirect('profile/login')
