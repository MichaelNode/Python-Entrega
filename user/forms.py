from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):

    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User {0} already exists'.format(username))
        return username
