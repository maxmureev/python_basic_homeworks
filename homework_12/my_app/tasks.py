from celery import shared_task
import os
from django.utils import timezone
from .models import Product


@shared_task
def send_notification(product_id):
    """Логирование создания нового товара (упрощенная версия)"""
    try:
        product = Product.objects.get(id=product_id)
        message = f"New product added. Name: {product.name}, id: {product.id}, price: {product.price}"
        print(message)
        timestamp = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("add_product.log", "a") as f:
            f.write(timestamp + ": " + message + "\n")
        return message
    except Product.DoesNotExist:
        error_msg = f"Товар с ID {product_id} не найден"
        print(error_msg)
        return error_msg
