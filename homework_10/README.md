# Python Developer. Basic, 09.2024

## Homework 10 (Django 3/4)

### Домашнее задание "Class-Based Views и тестирование"

#### Цель

Закрепить навыки работы с CBV (Class-Based Views) и написания автотестов с использованием Pytest.

#### Результат

Приложение интернет-магазина с функциональностью CRUD через CBV и тестами для ключевых функций.

#### Задача

Описание/Пошаговая инструкция выполнения домашнего задания:

1. Реализовать CBV
   + Использовать ListView для отображения списка товаров.
   + Настроить DetailView для отображения деталей товара.
   + Реализовать CreateView и UpdateView для добавления и редактирования товаров.
   + Добавить DeleteView для удаления товара.

1. Написать тесты для приложения
   + Тесты для моделей: проверить операции создания, чтения, обновления и удаления записей.

#### Критерии оценки

+ Реализованы CBV для CRUD-операций.
+ Написаны тесты.

---

### Install Django and create project

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

Migration

```shell
# Create migration
python manage.py makemigrations
# Apply all migrations
python manage.py migrate
# Fill the DB with test data
python manage.py fill_db
```

Install packages for tests

```shell
poetry add --group test pytest pytest-django pytest-mock
```

Run tests

```shell
pytest [-v]
 ```

Для работы с реальной БД

```shell
pytest --reuse-db
```
