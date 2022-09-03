from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from adminapp.forms import ProductEditForm
from mainapp.models import ProductCategory, Product
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls.base import reverse_lazy


# def product_create(request, pk):
#     title = 'продукт/создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[category.pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#     content = {'title': title,
#                'update_form': product_form,
#                'category': category
#                }
#
#     return render(request, 'adminapp/product_form.html', content)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_form.html'
    success_url = reverse_lazy('admin:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/создание'
        context['category'] = self.kwargs['pk']
        return context


# def products(request, pk):
#     title = 'админка/продукт'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list
#     }
#     return render(request, 'adminapp/products.html', content)

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk']).order_by('price')


# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     content = {'title': title, 'object': product, }
#
#     return render(request, 'adminapp/product_read.html', content)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     content = {'title': title,
#                'update_form': edit_form,
#                'category': edit_product.category
#                }
#
#     return render(request, 'adminapp/product_form.html', content)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_form.html'
    success_url = reverse_lazy('admin:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/редактирование'
        context['category'] = self.object.category.pk
        return context


# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#
#     content = {'title': title, 'product_to_delete': product}
#
#     return render(request, 'adminapp/product_delete.html', content)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:categories')

    def form_valid(self, form):
        success_url = self.get_success_url()
        # self.object.delete()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/удаление'
        return context
