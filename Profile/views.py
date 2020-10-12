from django.shortcuts import render, HttpResponse, redirect
from .forms import update_person_form
from django.contrib.auth.forms import UserCreationForm
from .models import Person
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def register_user_view(request):
    rp_form = UserCreationForm(request.POST or None)

    if rp_form.is_valid():
        rp_form.save()
        username = rp_form.cleaned_data.get('username')
        password = rp_form.cleaned_data.get('password1')
        messages.success(request, "The user " + username + " has been created")
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('Profile:update_url')

    para = {
        'rp_form': rp_form
    }

    return render(request, 'Profile/register.html', para)


def login_person_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Profile:myprofile_url')
        else:
            messages.info(request, "Username or Password is incorrect")
    return render(request, 'Profile/login.html')


def update_person_view(request):
    person = Person.objects.get(user=request.user)
    up_form = update_person_form(
        request.POST or None, request.FILES or None, instance=person)

    if up_form.is_valid():
        up_form.save()
        return redirect('Profile:myprofile_url')

    para = {
        'up_form': up_form,
    }

    return render(request, 'Profile/update.html', para)


def logout_person_view(request):
    logout(request)
    return redirect("Profile:login_url")


def home_page_view(request):
    user = request.user

    profile = Person.objects.get(user=user)

    para = {
        'profile': profile
    }

    return render(request, 'Profile/home.html', para)
