import pytest
from my_app.models import Product, Category


# Заполнение БД тестовыми данными
# Далее создается одна категория и один товар в этой категории


@pytest.fixture
def category():
    """Заполнение БД. Тестовая Категория"""
    return Category.objects.create(name="Категория из fixture")


@pytest.fixture
def product(category):
    """Заполнение БД. Товар с тестовыми данными"""
    return Product.objects.create(
        name="Товар из fixture",
        description="Описание тестового товара из fixture",
        # TODO: По какой-то причине тест падает при количестве символов в price > 8, когда в модели указано 10.
        # TODO: Вероятно каким-то образом учитываютя и символы после запятой
        price=111,
        category=category,
    )
