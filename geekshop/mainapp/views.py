from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404


def main(request):
    title = 'магазин'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/shop.html', content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products_list.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def product(request, pk):
    product = Product.objects.filter(pk=pk)
    content = {'products': product}
    return render(request, 'mainapp/product-page.html', content)






