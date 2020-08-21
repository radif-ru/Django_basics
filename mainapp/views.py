from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def showroom(request):
    return render(request, 'mainapp/showroom.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
