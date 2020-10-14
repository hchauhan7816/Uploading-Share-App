from django import forms
from .models import Post, Comment


class create_post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['picture']


class create_comment_form(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Add a comment...',
        'style': 'width: 630px;'
    }))

    class Meta:
        model = Comment
        fields = ['content']
