from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Like
from django.contrib.auth.decorators import login_required
from Profile.models import Person
from .forms import create_post_form, create_comment_form

# Create your views here.


@login_required(login_url="Profile:login_url")
def all_posts_view(request, x):

    cp_form = create_post_form()
    cc_form = create_comment_form()

    if 'submit_post_form' in request.POST:
        cp_form = create_post_form(request.POST, request.FILES)
        if cp_form.is_valid():
            instance = cp_form.save(commit=False)
            instance.author = Person.objects.get(user=request.user)
            instance.save()
            cp_form = create_post_form()

    if 'submit_comment_form' in request.POST:
        cc_form = create_comment_form(request.POST)
        if cc_form.is_valid():
            print("here")
            post_pk = request.POST.get('liked_id_2')
            print(post_pk)
            instance = cc_form.save(commit=False)
            instance.by_person = Person.objects.get(user=request.user)
            instance.on_post = Post.objects.get(pk=post_pk)
            instance.save()
            cc_form = create_comment_form()

    if x == 1:
        all_posts = Post.objects.all().order_by("-updated")
        # all_posts = Post.objects.all()
    else:
        this_person = Person.objects.get(user=request.user)
        temp_posts = Post.objects.all().order_by("-updated")
        all_posts = []

        for t in temp_posts:
            if t.author.user in this_person.following.all():
                all_posts.append(t)

    para = {
        'all_posts': all_posts,
        'cp_form': cp_form,
        'cc_form': cc_form,
        'profile': Person.objects.get(user=request.user),
        'y': x
    }

    return render(request, 'Posts/explore.html', para)


@login_required(login_url="Profile:login_url")
def liked_by_user_view(request, x):
    post_id = request.POST.get('liked_id')
    post = Post.objects.get(pk=post_id)
    user = Person.objects.get(user=request.user)

    if user not in post.likes.all():
        post.likes.add(user)
    else:
        post.likes.remove(user)

    if x == 1:
        return redirect("/posts/explore/1")
    else:
        return redirect("/posts/explore/2")
