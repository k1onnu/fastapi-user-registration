# FastAPI User Registration Service

Сервис регистрации пользователей с валидацией данных на FastAPI и Pydantic.

## Содержание
- [О проекте](#о-проекте)
- [Стек технологий](#стек-технологий)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [API Endpoints](#api-endpoints)
- [Валидация данных](#валидация-данных)
- [Тестирование](#тестирование)
- [Домашнее задание](#домашнее-задание)

## О проекте
Учебный проект по курсу "Разработка прототипов программных решений". 
Реализует REST API для регистрации пользователей с расширенной валидацией данных.

**Задания:**
1. Базовая регистрация (username, email, password, age)
2. Дополнительные поля (full_name, phone)
3. Рекурсивная модель для вложенных JSON

## Стек технологий
- Python 
- FastAPI 
- Pydantic 
- Uvicorn 
- Pytest 

## Структура проекта
```
fastapi-user-registration/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── registration.py  # Эндпоинты регистрации
│   │       └── nested.py         # Эндпоинты для дерева
│   ├── models/
│   │   ├── user.py               # Модель пользователя
│   │   └── tree.py                # Рекурсивная модель
│   ├── schemas/
│   │   └── responses.py           # Схемы ответов
│   ├── services/
│   │   ├── registration_service.py # Логика регистрации
│   │   └── tree_service.py         # Логика дерева
│   └── main.py                     # Точка входа
├── tests/
│   ├── test_registration.py
│   ├── test_tree.py
│   └── test_validation.py
├── requirements.txt
└── README.md
```

## Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/your-username/fastapi-user-registration.git
cd fastapi-user-registration
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск сервера
```bash
python -m app.main
# или
uvicorn app.main:app --reload
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

## API Endpoints

### Регистрация пользователя
```http
POST /register/
```

**Тело запроса:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "Password123",
    "password_confirm": "Password123",
    "age": 25,
    "full_name": "John Doe",
    "phone": "+7-999-123-45-67"
}
```

**Успешный ответ (200):**
```json
{
    "status": "success",
    "message": "Пользователь успешно зарегистрирован",
    "user": {
        "username": "john_doe",
        "email": "john@example.com",
        "age": 25,
        "registration_date": "2026-03-15T22:35:41.123456",
        "full_name": "John Doe",
        "phone": "+7-999-123-45-67"
    }
}
```

**Ответ с ошибкой (400):**
```json
{
    "status": "error",
    "message": "Ошибка валидации данных",
    "errors": [
        {
            "field": "password",
            "message": "Пароль должен содержать хотя бы одну заглавную букву"
        }
    ]
}
```

### Вложенная структура
```http
GET /nested/?depth=3
```

**Ответ:**
```json
{
    "data": "any_data_1",
    "child": {
        "data": "any_data_2",
        "child": {
            "data": "any_data_3",
            "child": null
        }
    }
}
```

## Валидация данных

### Поля и требования

| Поле | Тип | Требования |
|------|-----|------------|
| `username` | string | 3-20 символов, латиница, цифры, _ |
| `email` | email | Валидный email адрес |
| `password` | string | ≥8 символов, заглавная, строчная, цифра |
| `password_confirm` | string | Должен совпадать с password |
| `age` | integer | 18-120 лет |
| `full_name` | string | ≥2 символа, с заглавной буквы |
| `phone` | string | Формат: +X-XXX-XXX-XX-XX или +X-XXX-XX-XX |

### Примеры ошибок
- `"Пароль должен содержать хотя бы одну цифру"`
- `"Телефон должен начинаться с + и содержать только цифры и дефисы"`
- `"Полное имя должно начинаться с заглавной буквы"`

## Тестирование

### Запуск всех тестов
```bash
pytest tests/ -v
```

### Запуск конкретных тестов
```bash
# Тесты регистрации
pytest tests/test_registration.py -v

# Тесты дерева
pytest tests/test_tree.py -v

# Тесты валидации
pytest tests/test_validation.py -v
```

### Результаты тестов
```
collected 8 items

tests/test_registration.py::test_successful_registration PASSED
tests/test_registration.py::test_failed_registration PASSED
tests/test_registration.py::test_registration_with_missing_field PASSED
tests/test_tree.py::test_tree_creation PASSED
tests/test_tree.py::test_tree_depth_zero PASSED
tests/test_tree.py::test_tree_custom_prefix PASSED
tests/test_validation.py::test_username_validation PASSED
tests/test_validation.py::test_password_validation PASSED

8 passed in 0.14s
```

## Домашнее задание

### Задание 1 
- [x] Все поля с правильными типами и валидаторами
- [x] Кастомные проверки (username, пароль, возраст, дата)
- [x] Функция register_user с обработкой ошибок

### Задание 2 
- [x] Добавлены поля full_name и phone
- [x] Валидация full_name (заглавная буква, минимум 2 символа)
- [x] Валидация phone (формат +X-XXX-XX-XX)
- [x] Совместимость с валидациями из задания 1

### Задание 3 
- [x] Рекурсивная Pydantic-модель
- [x] Функция возвращает JSON с произвольной вложенностью
- [x] Нет ошибок циклических ссылок