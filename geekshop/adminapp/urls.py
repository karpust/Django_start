from django.urls import path, include
import adminapp.views.user_views as user
import adminapp.views.category_views as category
import adminapp.views.product_views as product

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.user_create, name='user_create'),
    path('users/read/', user.users, name='users'),
    path('users/update/<int:pk>/', user.user_update, name='user_update'),
    path('users/delete/<int:pk>/', user.user_delete, name='user_delete'),


    path('categories/', include([
        path('create/', category.category_create, name='category_create'),
        path('read/', category.categories, name='categories'),
        path('update/<int:pk>/', category.category_update, name='category_update'),
        path('delete/<int:pk>/', category.category_delete, name='category_delete'),
    ])),

    path('products/', include([
        path('create/category/<int:pk>/', product.product_create, name='product_create'),
        path('read/category/<int:pk>/', product.products, name='products'),
        path('read/<int:pk>/', product.product_read, name='product_read'),
        path('update/category/<int:pk>/', product.product_update, name='product_update'),
        path('delete/category/<int:pk>/', product.product_delete, name='product_delete'),
    ])),
]

