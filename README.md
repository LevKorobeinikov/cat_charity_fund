# Приложение QRKot

## Описание
Приложение для Благотворительного фонда поддержки котиков QRKot.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии 
- **Python 3.9** 
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Alembic**
- **Pydantic**
- **Uvicorn**

## Запуск

1. Клонирование репозитория:
    ```bash
    git clone git@github.com:LevKorobeinikov/cat_charity_fund.git
    cd cat_charity_fund
    ```

2. Создать и активировать виртуальное окружение:

    Для Windows:
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
    Для Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Установка зависимостей:
    ```bach
    pip install -r requirements.txt
    ```
4. Создайте файл с переменными окружения .env. Укажите в файле значения локальных переменных, представленных в образце .env.example
    ```bach
    touch .env
    ```
5. Примените миграции и запустите проект.
    ```bach
    alembic upgrade
    uvicorn app.main:app --reload 
    ```


## Автор проекта - [Коробейников Лев Сергеевич](https://github.com/LevKorobeinikov)
