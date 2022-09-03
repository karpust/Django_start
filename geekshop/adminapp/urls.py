from django.urls import path, include
import adminapp.views.user_views as user
import adminapp.views.category_views as category
import adminapp.views.product_views as product

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.UserCreateView.as_view(), name='user_create'),
    path('users/read/', user.UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UserDeleteView.as_view(), name='user_delete'),


    path('categories/', include([
        path('create/', category.CategoryCreateView.as_view(
            extra_context={'title': 'админка/создание'}), name='category_create'),
        path('read/', category.CategoryListView.as_view(
            extra_context={'title': 'админка/категории'}), name='categories'),
        path('update/<int:pk>/', category.CategoryUpdateView.as_view(
            extra_context={'title': 'админка/редактирование'}), name='category_update'),
        path('delete/<int:pk>/', category.CategoryDeleteView.as_view(
            extra_context={'title': 'админка/удаление'}), name='category_delete'),
    ])),

    path('products/', include([
        path('create/category/<int:pk>/', product.ProductCreateView.as_view(), name='product_create'),
        path('read/category/<int:pk>/', product.ProductListView.as_view(), name='products'),
        path('read/<int:pk>/', product.ProductDetailView.as_view(), name='product_read'),
        path('update/category/<int:pk>/', product.ProductUpdateView.as_view(), name='product_update'),
        path('delete/category/<int:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),
    ])),
]

