from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

class PostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {'tags': TagWidget()}

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
