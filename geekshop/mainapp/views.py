from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
import random


def main(request):
    title = 'магазин'
    products = Product.objects.all()
    basket = get_basket(request.user)
    content = {'title': title, 'products': products, 'basket': basket}
    return render(request, 'mainapp/shop.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', content)


def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user). \
        order_by('product__category')

    content = {
        'title': title,
        'basket': basket_items,
    }
    return render(request, 'basketapp/basket.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
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

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'конакты'
    basket = get_basket(request.user)
    content = {'title': title, 'basket': basket}
    return render(request, 'mainapp/contact.html', content)








