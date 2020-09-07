from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from basketapp.models import BasketItem
from mainapp.models import Product
from mainapp.views import LINKS_MENU, get_categories
from shop.settings import MEDIA_URL


@login_required
def index(request):
    # basket_items = BasketItem.objects.filter(user=request.user)
    # basket_items = request.user.basketitem_set.all()
    # при добавлении related_name в модель .._set перестаёт работать, работает заданное имя:
    basket_items = request.user.user_basket.all()
    context = {
        'page_title': 'корзина',
        'links_menu': LINKS_MENU,
        'media_url': MEDIA_URL,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, pk):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('auth:login'))

    # print(pk, type(pk))
    product = get_object_or_404(Product, pk=pk)
    basket = BasketItem.objects.filter(user=request.user, product=product).first()
    # basket = request.user.basketitem_set.filter(product=pk).first()

    if not basket:
        basket = BasketItem(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, pk):
    get_object_or_404(BasketItem, pk=pk).delete()
    return HttpResponseRedirect(reverse('basket:index'))