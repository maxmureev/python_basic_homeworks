# Python Developer. Basic, 09.2024

## Homeworks 08 (Django 1/4)

### Домашнее задание "Создание проекта, работа с моделями и продвинутая настройка админки"

#### Цель

Закрепить навыки создания проекта и приложения в Django, работы с моделями через ORM, а также настройки админки для удобной работы с данными.

#### Результат

Рабочий проект Django с подключённой базой данных, продвинутой настройкой админки, кастомными командами и генерацией данных через фабрики.

#### Задача

Описание/Пошаговая инструкция выполнения домашнего задания:

1. Создать Django проект и приложение:
    - Настроить новый проект Django.
    - Добавить приложение (например, store).
1. Создать модели
    - Модель Product с полями: name, description, price, created_at.
    - Модель Category с полями: name, description.
    - Связать Product с Category через ForeignKey.
1. Выполнить миграции
    - Создать и применить миграции.
1. Работа с ORM
    - Создать записи для моделей, используя кастомную команду.

Критерии оценки:

- Создание проекта и настройка моделей

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
