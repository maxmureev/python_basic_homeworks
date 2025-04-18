# Python Developer. Basic, 09.2024

## Homeworks 04. Базовый фронтенд. Веб-приложение на FastAPI

#### Задача

- скопируйте папку `homework_05` для этой домашки (Памятка: <https://github.com/OtusTeam/BasePython/tree/homeworks>)
- используйте следующие пакеты:
  - FastAPI
  - uvicorn
- в модуле `app` создайте базовое FastAPI приложение
- создайте обычные представления
  - создайте index view `/`
  - добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике
  - создайте базовый шаблон (используйте <https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template>)
  - в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
  - в базовый шаблон добавьте навигационную панель `nav` (<https://getbootstrap.com/docs/5.0/components/navbar/>)
  - в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
  - добавьте новые зависимости в файл `requirements.txt` в корне проекта
    (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
- создайте api представления:
  - создайте api router, укажите префикс `/api`
  - добавьте вложенный роутер для вашей сущности (если не можете придумать тип сущности, рассмотрите варианты: товар, книга, автомобиль)
  - добавьте представление для чтения списка сущностей
  - добавьте представление для чтения сущности
  - добавьте представление для создания сущности

#### Критерии оценки

- создано FastAPI приложение в `app.py`
- добавлен отдельный роутер для HTML представлений `/` и `/about/`
- добавлен api роутер
- добавлен роутер для ваших сущностей
- подключены и применены стили Bootstrap
- в базовый шаблон добавлена навигационная панель
- автоматический тест `test_homework_05` проходит

### Запуск

Зависимости

```shell
cd homework_04
pip install -r requirements.txt
```

Запуск

```shell
uvicorn app:app --reload
```
