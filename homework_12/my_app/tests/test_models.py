import pytest
from django.core.exceptions import ObjectDoesNotExist
from my_app.models import Product, Category


# ===== Тесты для модели Category =====
@pytest.mark.django_db
def test_category_creation(category):
    """Проверка создания категории (Create)"""
    assert Category.objects.count() == 1
    assert category.name == "Категория из fixture"
    assert str(category) == "Категория из fixture"


@pytest.mark.django_db
def test_category_read(category):
    """Проверка чтения категории (Read)"""
    retrieved = Category.objects.get(id=category.id)
    assert retrieved == category
    assert retrieved.name == "Категория из fixture"


@pytest.mark.django_db
def test_category_update(category):
    """Проверка обновления категории (Update)"""
    category.name = "Обновленная категория"
    category.save()
    updated = Category.objects.get(id=category.id)
    assert updated.name == "Обновленная категория"


@pytest.mark.django_db
def test_category_delete(category):
    """Проверка удаления категории (Delete)"""
    category_id = category.id
    category.delete()
    with pytest.raises(ObjectDoesNotExist):
        Category.objects.get(id=category_id)
    assert Category.objects.count() == 0


# ===== Тесты для модели Product =====
@pytest.mark.django_db
def test_product_creation(product):
    """Проверка создания товара (Create)"""
    assert Product.objects.count() == 1
    assert product.name == "Товар из fixture"
    assert str(product) == "Товар из fixture"
    assert product.price == 111
    assert product.description == "Описание тестового товара из fixture"


@pytest.mark.django_db
def test_product_read(product):
    """Проверка чтения товара (Read)"""
    retrieved = Product.objects.get(id=product.id)
    assert retrieved == product
    assert retrieved.name == "Товар из fixture"
    assert retrieved.price == 111


@pytest.mark.django_db
def test_product_update(product):
    """Проверка обновления товара (Update)"""
    product.name = "Обновленный товар"
    product.price = 222
    product.save()
    updated = Product.objects.get(id=product.id)
    assert updated.name == "Обновленный товар"
    assert updated.price == 222


@pytest.mark.django_db
def test_product_delete(product):
    """Проверка удаления товара (Delete)"""
    product_id = product.id
    product.delete()
    with pytest.raises(ObjectDoesNotExist):
        Product.objects.get(id=product_id)
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_product_category_relation(product, category):
    """Проверка связи товара с категорией"""
    product.category = category
    product.save()
    assert product.category == category
    assert category.products.count() >= 1
