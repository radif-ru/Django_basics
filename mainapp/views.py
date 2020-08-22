from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'INTERIOR',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Products',
    }
    return render(request, 'mainapp/products.html', context)


def showroom(request):
    context = {
        'page_title': 'Showroom',
    }
    return render(request, 'mainapp/showroom.html', context)


def contact(request):
    context = {
        'page_title': 'Contact',
    }
    return render(request, 'mainapp/contact.html', context)
