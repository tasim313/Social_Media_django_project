from django import forms
from .models import Posts, Like


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image', 'caption')