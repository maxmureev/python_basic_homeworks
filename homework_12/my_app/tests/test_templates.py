import pytest
from django.urls import reverse
from my_app.models import Product, Category
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_product_list_view(client, category, product):
    """Проверка списка товаров"""
    Product.objects.create(
        name="Тестовый товар из темплейта",
        description="Описание тестового товара из темплейта",
        price=333,
        category=category,
    )

    url = reverse("products_list")
    response = client.get(url)
    assert response.status_code == 200

    assert "Тестовый товар" in response.content.decode("utf-8")
    assert "Тестовый товар из темплейта" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_product_list_view_bs(client, category, product):
    """Проверка списка товаров c помощью bs"""
    Product.objects.create(
        name="Тестовый товар из темплейта BS",
        description="Описание тестового товара из темплейта BS",
        price=444,
        category=category,
    )

    url = reverse("products_list")
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.h3.text == "Список товаров"

    table = soup.find("table", class_="table")
    assert table is not None

    headers = [th.text.strip() for th in table.find("thead").find_all("th")]
    assert headers == ["Название", "Описание", "Цена", "Провалиться"]

    rows = table.find("tbody").find_all("tr")
    assert len(rows) == 2  # Один товар из фикстуры + только что созданный

    cells = rows[1].find_all("td")
    assert cells[0].text.strip() == "Тестовый товар из темплейта BS"
    assert cells[1].text.strip() == "Описание тестового товара из темплейта BS"
    assert cells[2].text.strip() in ["444", "444.00"]
