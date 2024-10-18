# Веб-сервис на Django для парсинга HTML-страниц(Тестовое задание)

## Технологии
- **Python**
- **Django**
- **PostgreSQL**

## Установка и настройка
### 1. Клонируйте репозиторий:
```sh
git clone https://github.com/G-Ilkhom/test_task.git
```
### 2. Перейдите в директорию проекта и создайте виртуальное окружение:
```sh
cd test_task
```
```sh
python -m venv venv
```

### 3. Активируйте виртуальное окружение:
- На Windows:
```sh
venv\Scripts\activate
```
- На Unix или MacOS:
```sh
source venv/bin/activate
```
### 4. Установите зависимости:
```sh
pip install -r requirements.txt
```
### 5. Создайте и примените миграции:
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```

### 6. Запустите сервер:
```sh
python manage.py runserver
```
