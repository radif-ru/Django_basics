from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserAuthenticationForm, ShopUserRegisterForm, ShopUserProfileForm


def login(request):
    # print(request.method)
    if request.method == 'POST':
        # print('data:', request.POST)
        form = ShopUserAuthenticationForm(data=request.POST)
        if form.is_valid():  # errors dict
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect('/')  # хардкод, лучше так не делать
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserAuthenticationForm()
    context = {
        'page_title': 'аутентификация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def user_register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(data=request.POST, files=request.FILES)
        if register_form.is_valid():  # errors dict
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    context = {
        'page_title': 'регистрация',
        'form': register_form
    }

    return render(request, 'authapp/user_register.html', context)


def user_profile(request):
    form = ShopUserProfileForm()
    context = {
        'page_title': 'профиль',
        'form': form
    }
    return render(request, 'authapp/login.html', context)
