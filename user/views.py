from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from user.forms import SignInForm


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong username or password')
        else:
            login_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)

        return render(request, 'users/login.html')


class Logout(View):

    def get(self, request):
        finish_user_session(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')


class SignInView(View):

    def get(self, request):
        form = SignInForm()
        return render(request, 'users/signin.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered successfully!')
            login_user_in_django(request, new_user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)
        return render(request, 'users/signin.html', {'form': form})
