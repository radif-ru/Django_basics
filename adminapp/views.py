from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, \
    AdminProductCategoryCreateForm
from mainapp.models import ProductCategory
from shop.settings import MEDIA_URL


# Незалогиненного отправляем логинится. Проверяем является ли пользователь суперюзером
# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     users_list = get_user_model().objects.all().order_by(
#         '-is_active', '-is_superuser', '-is_staff', 'username'
#     )
#
#     context = {
#         'page_title': 'админка/пользователи',
#         'users_list': users_list,
#         'media_url': MEDIA_URL
#     }
#
#     return render(request, 'adminapp/index.html', context)


class OnlySuperUserMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        # print(data)
        data['page_title'] = self.page_title
        return data


class MediaUrlMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['media_url'] = self.media_url
        return data


class UsersList(OnlySuperUserMixin, PageTitleMixin, MediaUrlMixin, ListView):
    model = get_user_model()

    page_title = 'админка/пользователи'
    media_url = MEDIA_URL

    # extra_context = {
    #     'page_title': 'админка/пользователи',
    #     'media_url': MEDIA_URL
    # }

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs
    #     # return self.model.objects.all().order_by()


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
        'page_title': 'пользователи/создание',
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
        'page_title': 'пользователи/редактирование',
        'user_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    # user.delete()
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:index'))

    context = {
        'page_title': 'пользователи/удаление',
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', context)


# @user_passes_test(lambda x: x.is_superuser)
# def categories_read(request):
#     context = {
#         'page_title': 'админка/категории',
#         'categories_list': ProductCategory.objects.all(),
#     }
#
#     return render(request, 'adminapp/categories_list.html', context)

# FBS vs CBV


# class CategoriesRead(ListView):
#     model = ProductCategory
#     template_name = 'adminapp/categories_list.html'
#     context_object_name = 'categories_list'


# class CategoriesRead(ListView):
#     model = ProductCategory
#     template_name = 'adminapp/categories_list.html'


class ProductCategoriesRead(OnlySuperUserMixin, PageTitleMixin, ListView):
    model = ProductCategory
    page_title = 'админка/категории'
    # extra_context = {
    #     'page_title': 'админка/категории',
    # }


class ProductCategoryCreate(OnlySuperUserMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    page_title = 'админка/категории/создание'
    # success_url = reverse('my_admin:index')
    success_url = reverse_lazy('my_admin:index')
    # fields = '__all__'
    form_class = AdminProductCategoryCreateForm
