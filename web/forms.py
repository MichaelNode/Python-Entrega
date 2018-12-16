from django import forms
from web.models import *

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'description'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': ''})
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [

            'cat_id',
            'title',
            'content',
            'image',
            'status'
        ]

        widgets = {

            'cat_id' : forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'status': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'title'  : forms.TextInput(attrs={'class': 'form-control', 'required': ''}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'required': ''}),
            'image'  : forms.FileInput(attrs={ 'required': ''})

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'title',
            'content'
        ]
