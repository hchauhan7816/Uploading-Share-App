from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Like
from django.contrib.auth.decorators import login_required
from Profile.models import Person
from .forms import create_post_form

# Create your views here.


@login_required(login_url="Profile:login_url")
def all_posts_view(request):

    cp_form = create_post_form(request.POST or None, request.FILES or None)

    if cp_form.is_valid():
        instance = cp_form.save(commit=False)
        instance.author = Person.objects.get(user=request.user)
        instance.save()
        cp_form = create_post_form()

    all_posts = Post.objects.all().order_by("-updated")
    # all_posts = Post.objects.all()

    para = {
        'all_posts': all_posts,
        'cp_form': cp_form,
        'profile' : Person.objects.get(user = request.user)
    }

    return render(request, 'Posts/explore.html', para)


@login_required(login_url="Profile:login_url")
def following_posts_view(request):
    this_person = Person.objects.get(user=request.user)
    all_posts = Post.objects.all().order_by("-updated")
    valid_posts = []

    for x in all_posts:
        if x.author.user in this_person.following.all():
            valid_posts.append(x)

    para = {
        'all_posts': valid_posts,
    }

    return render(request, 'Posts/friend_post.html', para)


@login_required(login_url="Profile:login_url")
def liked_by_user_view(request):
    post_id = request.POST.get('liked_id')
    post = Post.objects.get(pk=post_id)
    user = Person.objects.get(user=request.user)

    if user not in post.likes.all():
        post.likes.add(user)
    else:
        post.likes.remove(user)

    return redirect("Posts:all_posts_url")
