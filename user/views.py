from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import RegisterForm, User, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Hisob ochildi {user.username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Hisobingizga kirdingiz!')
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    messages.warning(request, f'Hisobdan chiqildi!')
    return redirect('login')

