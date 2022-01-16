from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from user.forms import RegisterForm
from user.models import CustomUser


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Registration error!")
            return HttpResponseRedirect('/')
    form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Error!')
            return redirect('login')
    return render(request, 'user/login.html')


def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')


def my_profile(request):
    user = CustomUser.objects.get(username=request.user.username)
    return render(request, 'user/my_profile.html', {'user': user})
