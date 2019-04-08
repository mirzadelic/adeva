# Adeva API

# Install:
Use `virtualenv` or `pyenv` to create separated python environment, and use `python 3`.
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# External API urls:
 - `http://localhost:8000/api/external/books/` - List all books from external call
 - `http://localhost:8000/api/external/books/?name=A Clash of Kings` - List all books from external call with a name `A Clash of Kings`
