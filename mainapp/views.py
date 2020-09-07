import json
import os

from django.shortcuts import render, get_object_or_404

from basketapp.models import BasketItem
from mainapp.models import ProductCategory, Product
from shop.settings import BASE_DIR, JSON_PATH, MEDIA_URL

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/links_menu.json'),
          encoding="utf-8") as f:
    LINKS_MENU = json.loads(f.read())

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/contact_locations.json'),
          encoding="utf-8") as f:
    LOCATIONS = json.loads(f.read())


def get_categories():
    return ProductCategory.objects.all()


def get_user_basket(request):
    quantity = 0
    price = 0
    for item in BasketItem.objects.filter(user_id=request.user.id):
        quantity += item.quantity
        price += Product.objects.filter(id=item.product_id).first().price * quantity
    return f'{quantity}шт., на {price}р.'


def index(request):
    print(request.POST)
    featured_new_products = Product.objects.all().order_by('pk')
    products = Product.objects.all().order_by('price')
    context = {
        'page_title': 'INTERIOR',
        'links_menu': LINKS_MENU,
        'user_basket': get_user_basket(request),
        'products': products[:3],
        'media_url': MEDIA_URL,
        'featured_new_products': featured_new_products[:4],
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all().order_by('price')
    context = {
        'page_title': 'Products',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'user_basket': get_user_basket(request),
        'products': products[:3],
        'media_url': MEDIA_URL,
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request, pk=0):
    if pk == 0:
        category = {'pk': 0, 'name': 'all'}
        products = Product.objects.all().order_by('-pk')
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category).order_by('price')
    context = {
        'page_title': 'Showroom',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'user_basket': get_user_basket(request),
        'products': products[:6],
        'media_url': MEDIA_URL,
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
        'locations': LOCATIONS,
        'links_menu': LINKS_MENU,
        'user_basket': get_user_basket(request),
    }
    return render(request, 'mainapp/contact.html', context)


def catalog(request, pk):
    # try:
    #     category = ProductCategory.objects.get(pk=pk)
    # except ...
    if pk == 0:
        category = {'pk': 0, 'name': 'all'}
        products = Product.objects.all().order_by('price')
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category).order_by('price')
    context = {
        'page_title': 'Catalog',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'category': category,
        'featured_new_products': products,
        'media_url': MEDIA_URL,
        'user_basket': get_user_basket(request),
    }
    return render(request, 'mainapp/catalog.html', context)
