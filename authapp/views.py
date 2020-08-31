from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import MyAuthenticationForm


def login(request):
    # print(request.method)
    form = None
    if request.method == 'POST':
        # print('data:', request.POST)
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():  # errors dict
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect('/')
                return HttpResponseRedirect(reverse('main:index'))
    elif request.method == 'GET':
        form = MyAuthenticationForm()
    context = {
        'page_title': 'аутентификация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    pass


def register(request):
    pass
