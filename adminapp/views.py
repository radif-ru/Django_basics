from django.contrib.auth.decorators import user_passes_test


# Незалогиненного отправляем логинится. Проверяем является ли пользователь суперюзером
@user_passes_test(lambda x: x.is_superuser)
def index(request):
    pass
