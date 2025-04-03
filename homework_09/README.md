# Python Developer. Basic, 09.2024

## Homeworks 09 (Django 2)

### Домашнее задание "Создание проекта, работа с моделями и продвинутая настройка админки"

#### Цель

Закрепить навыки работы с HTML-шаблонами, передачи данных из контроллеров в шаблоны и реализации форм для пользовательского ввода.

#### Результат

Динамическое веб-приложение для интернет-магазина с отображением данных через шаблоны и возможностью добавления и редактирования товаров через формы.

#### Задача

Описание/Пошаговая инструкция выполнения домашнего задания:

1. Создать шаблоны
   - Настроить базовый шаблон с использованием block и extends.
   - Создать страницу списка товаров (Product), где отображаются название, описание и цена.
   - Настроить страницу деталей товара с выводом всех данных.
1. Создать формы
   - Настроить форму для добавления нового товара.
   - Настроить форму для редактирования товара.
1. Связь с шаблонами
   - Настроить отображение ошибок валидации в шаблонах.
   - Реализовать обработку пользовательского ввода через контроллеры.
1. Настроить админку
   - Добавить кастомизацию: list_display, list_filter, search_fields.
   - Создать кастомные действия через @admin.action. Например, поменять цену или опубликовать товар.

#### Критерии оценки

- Реализованы шаблоны для списка и деталей товаров.
- Формы работают корректно, включая валидацию.
- Настройка админки с кастомизацией.

#### Install Django and create project

Install Django and init Django project:

```shell
poetry init
poetry add django
django-admin startproject config .
```

Create and provisioning application:

```shell
python manage.py startapp my_app
python manage.py migrate
python manage.py createsuperuser
```

Run project with application:

```shell
python manage.py runserver
```

```shell
# Create migration
python manage.py makemigrations
# Apply all migrations
python manage.py migrate
# Fill the DB with test data
python manage.py fill_db
```
