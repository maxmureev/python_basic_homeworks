import pytest
from django.urls import reverse


def test_index_view(client):
    """Проверка главной страницы"""
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Go to" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_post_list_view(client, product, category):
    """Проверка списка товаров"""
    url = reverse("products_list")
    response = client.get(url)
    assert response.status_code == 200

    assert "Товар из fixture" in response.content.decode("utf-8")
    assert product.category == category
