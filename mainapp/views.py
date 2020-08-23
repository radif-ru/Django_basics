from django.shortcuts import render
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'mainapp/templates/mainapp/jsons/links_menu.json')) as f:
    links_menu = json.loads(f.read())


def index(request):
    context = {
        'page_title': 'INTERIOR',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Products',
        'add_class_names': ' exclusive_margin',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request):
    context = {
        'page_title': 'Showroom',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    with open(
            os.path.join(BASE_DIR, 'mainapp/templates/mainapp/jsons/contact_locations.json')) as f:
        locations = json.loads(f.read())

    context = {
        'page_title': 'Contact',
        'locations': locations,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', context)
