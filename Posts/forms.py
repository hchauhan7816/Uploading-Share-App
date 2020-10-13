from django.forms import ModelForm
from .models import Post


class create_post_form(ModelForm):
    class Meta:
        model = Post
        fields = ['picture']
