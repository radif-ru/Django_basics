import json
import os

from django.shortcuts import render, get_object_or_404

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


def index(request):
    context = {
        'page_title': 'INTERIOR',
        'links_menu': LINKS_MENU,
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Products',
        'links_menu': LINKS_MENU,
        'categories': get_categories()[:5],
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request):
    context = {
        'page_title': 'Showroom',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
        'locations': LOCATIONS,
        'links_menu': LINKS_MENU,
    }
    return render(request, 'mainapp/contact.html', context)


def catalog(request, pk):
    # try:
    #     category = ProductCategory.objects.get(pk=pk)
    # except ...
    if pk == 0:
        category = {'pk': 0, 'name': 'all'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)
    media_url = MEDIA_URL
    context = {
        'page_title': 'Catalog',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'category': category,
        'products': products,
        'media_url': media_url,
    }
    return render(request, 'mainapp/catalog.html', context)
