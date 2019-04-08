# Adeva API

# Install:
Use `virtualenv` or `pyenv` to create separated python environment, and use `python 3`.
Configure `.env.example` file with your Postgres settings and create database.
```
source .env.example
pip install -r requirements.txt
```

# Run:
```
python manage.py migrate && python manage.py runserver
```

# External API urls:
 - `http://localhost:8000/api/external/books/` - List all books from external api
 - `http://localhost:8000/api/external/books/?name=A Clash of Kings` - List all books from external call with a name `A Clash of Kings`

# Local API urls:
 - `GET` - `http://localhost:8000/api/local/books/` - List all books
 - `GET` - `http://localhost:8000/api/local/books/{id}/` - Detail book
 - `PUT`/`PATCH` - `http://localhost:8000/api/local/books/{id}/` - Update book
 - `DELETE` - `http://localhost:8000/api/local/books/{id}/` - Delete book
