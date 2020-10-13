from django.db import models
from Profile.models import Person
from django.core.validators import FileExtensionValidator

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='author_toh_dede')
    picture = models.ImageField(upload_to='picture', validators=[
                                FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=False)
    likes = models.ManyToManyField(Person, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.first_name}_{self.author.last_name}_{self.created.strftime('%d-%m-%y')}"

    def count_likes(self):
        return self.likes.all().count()


class Like(models.Model):
    like_to = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="like_kispr_dia")
    given_by = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="like_kisne_dia")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
