from .models import Post, Comment
from django import forms
from django.forms import ModelForm, TextInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'blog_image', 'slug', 'excerpt', 'content', 'status')  # noqa

        widgets = {
             'title': forms.TextInput(attrs={'placeholder': 'Enter your Title'}),  # noqa
             'excerpt': forms.TextInput(attrs={'placeholder': 'Enter a short Excerpt'}),  # noqa
             'content': SummernoteWidget(),

        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
