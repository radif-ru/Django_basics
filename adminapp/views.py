from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test


# Незалогиненного отправляем логинится. Проверяем является ли пользователь суперюзером
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm
from shop.settings import MEDIA_URL


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = get_user_model().objects.all().order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username'
    )

    context = {
        'page_title': 'админка/пользователи',
        'users_list': users_list,
        'media_url': MEDIA_URL
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'title': 'пользователи/создание',
        'user_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'title': 'пользователи/редактирование',
        'user_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)