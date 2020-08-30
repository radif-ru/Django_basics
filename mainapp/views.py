from django.shortcuts import render

from mainapp.models import ProductCategory
from shop.settings import BASE_DIR, JSON_PATH
import json
import os

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/links_menu.json'),
          encoding="utf-8") as f:
    LINKS_MENU = json.loads(f.read())

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/contact_locations.json'),
          encoding="utf-8") as f:
    LOCATIONS = json.loads(f.read())

CATEGORIES = ProductCategory.objects.all()


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
        'categories': CATEGORIES[:5],
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request):
    context = {
        'page_title': 'Showroom',
        'links_menu': LINKS_MENU,
        'categories': CATEGORIES,
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
        'locations': LOCATIONS,
        'links_menu': LINKS_MENU,
    }
    return render(request, 'mainapp/contact.html', context)
