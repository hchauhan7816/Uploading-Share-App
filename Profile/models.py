from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, blank=True)
    following = models.ManyToManyField(
        User, blank=True, related_name="following_in_model")
    bio = models.TextField(default="No Bio.", max_length=250)
    email = models.EmailField(blank=True, max_length=254)
    profile_pic = models.ImageField(
        default='avatar.png', upload_to='profile_pic')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}_{self.last_name}_{self.created.strftime('%d-%m-%y')}"

    def count_following(self):
        return self.following.all().count()
