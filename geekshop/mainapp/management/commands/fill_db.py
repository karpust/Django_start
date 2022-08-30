import json
import os
from django.conf import settings

# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product

from authapp.models import ShopUser

JSON_PATH = './mainapp/json/'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            print(product)
            category_id = product["category"]
            print(product["category"])
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(id=category_id)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        #     ShopUser.objects.all().delete()
            super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)

