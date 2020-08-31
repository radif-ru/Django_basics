from django.shortcuts import render

from authapp.forms import MyAuthenticationForm


def login(request):
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
