import json
import os
import random

from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product
from shop.settings import BASE_DIR, JSON_PATH, MEDIA_URL

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/links_menu.json'),
          encoding="utf-8") as f:
    LINKS_MENU = json.loads(f.read())

with open(os.path.join(BASE_DIR, f'{JSON_PATH}/contact_locations.json'),
          encoding="utf-8") as f:
    LOCATIONS = json.loads(f.read())


def get_hot_product():
    # products = Product.objects.all()
    # return random.choice(products)
    # Оптимизация запросов (нагрузки). Получаем все id, и из рандомного достаём объект
    products_id = Product.objects.values_list('id', flat=True)
    hot_product_id = random.choice(products_id)
    return Product.objects.get(pk=hot_product_id)


def related_products(product):
    return Product.objects.filter(category=product.category).exclude(id=product.id)


def get_categories():
    return ProductCategory.objects.all()


def index(request):
    print(request.POST)
    featured_new_products = Product.objects.all().order_by('pk')
    products = Product.objects.all().order_by('price')
    context = {
        'page_title': 'INTERIOR',
        'links_menu': LINKS_MENU,
        'products': products[:3],
        'media_url': MEDIA_URL,
        'featured_new_products': featured_new_products[:4],
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()
    _related_products = related_products(hot_product)

    products = Product.objects.all().order_by('price')
    context = {
        'page_title': 'Products',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'products': _related_products,
        'media_url': MEDIA_URL,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context)


def product_page(request, pk):
    context = {
        'page_title': 'продукт',
        'links_menu': LINKS_MENU,
        'categories': get_categories(),
        'product': get_object_or_404(Product, pk=pk),
        'media_url': MEDIA_URL,
    }
    return render(request, 'mainapp/product_page.html', context)


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
        'products': products,
        'media_url': MEDIA_URL,
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
    }
    return render(request, 'mainapp/catalog.html', context)
