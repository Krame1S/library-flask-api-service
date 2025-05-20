# Библиотечный API

REST API для управления книгами в библиотеке, построенный с помощью Python, Flask и PostgreSQL. Поддерживает CRUD-операции для книг (создание, чтение, обновление, удаление).

## Как запустить проект

1.  **Клонировать репозиторий:**

    ```bash
    git clone <https://github.com/Krame1S/library-flask-api-service>
    cd library_project
    ```

2.  **Создать и активировать виртуальное окружение:**

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3.  **Установить зависимости:**

    ```bash
    pip install flask psycopg2-binary python-dotenv
    ```

4.  **Настроить PostgreSQL:**

    - Создать базу данных `library`.
    - Выполнить SQL для создания таблицы:
      ```sql
      CREATE TABLE books (
          isbn VARCHAR(13) PRIMARY KEY,
          title VARCHAR(30) NOT NULL,
          copies_available INTEGER NOT NULL CHECK (copies_available >= 0)
      );
      ```

5.  **Настроить переменные окружения:**
    Создать файл `.env` в корне проекта:

    ```bash
    echo "DB_NAME=library" >> .env
    echo "DB_USER=your_username" >> .env
    echo "DB_PASS=your_password" >> .env
    echo "DB_HOST=localhost" >> .env
    ```

6.  **Запустить приложение:**
    ```bash
    python3 run.py
    ```
    API будет доступен на `http://127.0.0.1:5000`.

## Тестирование проекта

### Подготовка тестовых данных

Выполнить в `psql`:
`sql
     INSERT INTO books (isbn, title, copies_available) VALUES
     ('9781234567890', 'Book 1', 2),
     ('9780987654321', 'Book 2', 1);
     `

### API-запросы

- **GET /api/v1/books** — Получить список книг:

  ```bash
  curl http://127.0.0.1:5000/api/v1/books
  ```

  Ответ:

  ```json
  {
    "books": [
      { "isbn": "9781234567890", "title": "Book 1", "copies": 2 },
      { "isbn": "9780987654321", "title": "Book 2", "copies": 1 }
    ]
  }
  ```

- **POST /api/v1/books** — Создать книгу:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"isbn":"9782222222222","title":"Book 3","copies":3}' http://127.0.0.1:5000/api/v1/books
  ```

  Ответ:

  ```json
  { "message": "Book created successfully" }
  ```

- **PUT /api/v1/books/<isbn>** — Обновить книгу:

  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"title":"Book 1 updated","copies":5}' http://127.0.0.1:5000/api/v1/books/9781234567890
  ```

  Ответ:

  ```json
  { "message": "Book updated successfully" }
  ```

- **DELETE /api/v1/books/<isbn>** — Удалить книгу:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/v1/books/9782222222222
  ```
  Ответ:
  ```json
  { "message": "Book deleted successfully" }
  ```
