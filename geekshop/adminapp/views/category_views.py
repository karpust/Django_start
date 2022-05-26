from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from adminapp.forms import ProductCategoryEditForm
from mainapp.models import ProductCategory


def category_create(request):
    title = 'категории/создание'
    if request.method == 'POST':
        new_category = ProductCategoryEditForm(request.POST, request.FILES)
        if new_category.is_valid():
            new_category.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        new_category = ProductCategory()
    content = {
        'title': title,
        'update_form': new_category
    }
    return render(request, 'adminapp/category_update.html', content)


def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


def category_update(request, pk):
    title = 'категории/редактирование'

    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:category_update'))
    else:
        edit_form = ProductCategoryEditForm(instance=category)

    content = {
        'title': title,
        'update_form': edit_form
    }
    return render(request, 'adminapp/category_update.html', content)


def category_delete(request, pk):
    title = 'категории/удаление'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = 'False'
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))
    content = {
        'title': title,
        'category_to_delete': category
    }
    return render(request, 'adminapp/category_delete.html', content)
