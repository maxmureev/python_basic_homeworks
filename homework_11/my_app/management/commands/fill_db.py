from django.core.management.base import BaseCommand
from my_app.models import Category, Product


class Command(BaseCommand):
    help = "Заполняет базу данных тестовыми категориями и товарами"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        electronics = Category.objects.create(
            name="Электроника", description="Техника и гаджеты"
        )
        clothing = Category.objects.create(
            name="Одежда", description="Модная одежда и аксессуары"
        )

        Product.objects.create(
            name="iPhone 15",
            description="Смартфон с камерой 48 МП",
            price=999.99,
            category=electronics,
        )
        Product.objects.create(
            name="Смартфон",
            description="Флагманский смартфон",
            price=9999.99,
            category=electronics,
        )
        Product.objects.create(
            name="Джинсы",
            description="Классические синие джинсы",
            price=49.99,
            category=clothing,
        )

        self.stdout.write(self.style.SUCCESS("Успешно созданы тестовые данные!"))
