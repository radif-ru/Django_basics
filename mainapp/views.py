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
    locations = [
        # from json, from pickle, from db
        {
            'city': 'California',
            'phone': '1900 - 1234 - 5678',
            'email': 'info@interior.com',
            'address': '12 W 1st St, 90001 Los Angeles, California',
        },
        {
            'city': 'Texas',
            'phone': '1926 - 2314 - 3245',
            'email': 'texas@interior.com',
            'address': '24 W 1st St, 23554 Dallas County, Texas',
        },
        {
            'city': 'Georgia',
            'phone': '1999 - 2334 - 3457',
            'email': 'georgia@interior.com',
            'address': '23 W 1st St, 90001 Mogul, Georgia',
        },
    ]
    context = {
        'page_title': 'Contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
