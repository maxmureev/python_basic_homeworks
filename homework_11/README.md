# Python Developer. Basic, 09.2024

## Homework 11 (Django 4/4)

### Домашнее задание "Задачи с Celery и Redis"

#### Цель

Освоить использование Celery для выполнения фоновых задач и настройку Redis как брокера задач.

#### Результат

Приложение интернет-магазина с фоновыми задачами (например, отправка уведомлений при добавлении новых товаров).

#### Задача

Описание/Пошаговая инструкция выполнения домашнего задания:

1. Настроить Celery и Redis
   - Установить Celery и Redis.
   - Подключить Redis как брокер задач для Celery.

1. Реализовать фоновую задачу
   - Создать задачу для логирования информации о добавлении нового товара.
   - Задача должна выводить сообщение на консоль (например, название нового товара).

1. Протестировать Celery
   - Убедиться, что задачи корректно ставятся в очередь и выполняются.

#### Критерии оценки

- Настроен Celery с Redis.
- Реализована и протестирована фоновая задача.

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

Install celery

```shell
poetry add "celery[redis]" django-celery-results django-celery-beat
```

Run Redis with Docker

```shell
cd homework_11
docker compose up -d
```

Apply Celery migrations

```shell
python manage.py migrate
```

Check that Celery is working

```shell
cd homework_11
celery -A config worker --loglevel=info
```
