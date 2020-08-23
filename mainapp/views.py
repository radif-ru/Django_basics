from django.shortcuts import render
import json
import os


def index(request):
    context = {
        'page_title': 'INTERIOR',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Products',
        'exclusive_margin': ' exclusive_margin',
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request):
    context = {
        'page_title': 'Showroom',
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, 'mainapp/templates/mainapp/json/contact_locations.json')) as f:
        loc_json = f.read()

    locations = json.loads(loc_json)
    context = {
        'page_title': 'Contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
