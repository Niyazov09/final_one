# Task Tracker API

## Описание

Task Tracker API — это REST API, разработанное с использованием Django REST Framework. Приложение позволяет создавать проекты, управлять задачами, добавлять комментарии и работать с пользователями через JWT-аутентификацию.

---

## Используемые технологии

* Python 3
* Django
* Django REST Framework
* JWT (SimpleJWT)
* SQLite
* Django Filter
* DRF Spectacular (Swagger/OpenAPI)

---

## Возможности

* Авторизация по JWT
* Создание проектов
* Добавление участников в проект
* Создание задач
* Назначение исполнителей
* Комментирование задач
* Поиск задач
* Фильтрация задач
* Сортировка задач
* Пагинация
* Swagger документация API

---

## Установка

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать окружение:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Установить зависимости:

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-filter
pip install drf-spectacular
```

---

## Применить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Создать администратора

```bash
python manage.py createsuperuser
```

---

## Запуск проекта

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```
http://127.0.0.1:8000/
```

---

## JWT Авторизация

Получить токен:

```
POST /api/token/
```

Обновить токен:

```
POST /api/token/refresh/
```

---

## Основные API

### Проекты

```
GET    /api/projects/
POST   /api/projects/
PUT    /api/projects/{id}/
DELETE /api/projects/{id}/
POST   /api/projects/{id}/add_member/
```

### Задачи

```
GET    /api/tasks/
POST   /api/tasks/
PUT    /api/tasks/{id}/
DELETE /api/tasks/{id}/
GET    /api/tasks/{id}/comments/
```

### Комментарии

```
GET    /api/comments/
POST   /api/comments/
PUT    /api/comments/{id}/
DELETE /api/comments/{id}/
```

---

## Swagger документация

OpenAPI Schema:

```
/api/schema/
```

Swagger UI:

```
/api/schema/swagger-ui/
```

ReDoc:

```
/api/schema/redoc/
```

---

## Запуск тестов

```bash
python manage.py test
```

---

## Автор

Проект выполнен в рамках учебного задания по Django REST Framework.
