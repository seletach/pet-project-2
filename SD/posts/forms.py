from .models import Post, Comments
from django import forms


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('text',)