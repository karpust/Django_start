from django.shortcuts import render
from mainapp.models import Product


def main(request, pk=None):
    title = 'магазин'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    print(pk)
    return render(request, 'mainapp/shop.html', content)


def products(request, pk=None):
    title = 'каталог'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    print(pk)
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    title = 'контакты'
    content = {'title': title}
    return render(request, 'mainapp/contact.html', content)



