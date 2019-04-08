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
 - `http://localhost:8000/api/external/books/` - List all books from external call
 - `http://localhost:8000/api/external/books/?name=A Clash of Kings` - List all books from external call with a name `A Clash of Kings`
