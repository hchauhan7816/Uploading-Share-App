from django.forms import ModelForm
from .models import Post, Comment


class create_post_form(ModelForm):
    class Meta:
        model = Post
        fields = ['picture']


class create_comment_form(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
