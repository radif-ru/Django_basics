from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test


# Незалогиненного отправляем логинится. Проверяем является ли пользователь суперюзером
from django.shortcuts import render


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = get_user_model().objects.all().order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username'
    )

    context = {
        'page_title': 'админка/пользователи',
        'users_list': users_list
    }

    return render(request, 'adminapp/index.html', context)
