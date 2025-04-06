import pytest
from my_app.forms import ProductModelForm
from my_app.tests.conftest import Product, Category


@pytest.mark.django_db
def test_product_modelform_validation():
    """Проверка валидации модельной формы"""
    category = Category.objects.create(name="Категория из модели")
    form_data = {
        "name": "Товар из модели",
        "description": "Описание товара из модели",
        "category": category.id,
        "price": 222,
    }

    form = ProductModelForm(data=form_data)
    assert form.is_valid()
    product = form.save()
    assert product.name == form_data["name"]
