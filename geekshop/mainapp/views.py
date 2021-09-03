from django.shortcuts import render


def main(request):
    data = {'title': 'магазин'}
    return render(request, 'mainapp/shop.html', data)


def products(request):
    data = {'title': 'каталог'}
    return render(request, 'mainapp/catalog.html', data)


def contact(request):
    data = {'title': 'контакты'}
    return render(request, 'mainapp/contact.html', data)


# def temp(request):
#     return render(request, 'mainapp/temp1.html')

