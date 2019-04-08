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
 - `GET` - `http://localhost:8000/api/local/books/?date=2019` - List all books that are released at 2019 year, filters work with fields: `name`, `country`, `publisher`, `date`
 - `GET` - `http://localhost:8000/api/local/books/{id}/` - Detail book
 - `PUT`/`PATCH` - `http://localhost:8000/api/local/books/{id}/` - Update book
 - `DELETE` - `http://localhost:8000/api/local/books/{id}/` - Delete book

# Run Tests:
```
python manage.py test
```
