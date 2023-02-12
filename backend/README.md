# Backend structure
```python
├── README.md
├── apps
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── managers
│   │   ├── migrations
│   │   ├── models
│   │   │   ├── user.py
│   │   │   ├── ....
│   │   ├── tests.py
│   │   └── views.py
│   ├── api
│   │   ├── ... # for api
│   └── common
│       ├── ... # for common models, settings
│   └── ... # for another apps
├── core
│   ├── asgi.py
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── staging.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   ├── production.txt
│   └── test.txt
└── requirements.txt
```

# Configuration

# How to run

## Python
```python
python3 backend/manage.py makemigrations
python3 backend/manage.py migrate
python3 backend/manage.py runserver
```

## Celery
```python
cd backend
DJANGO_SETTINGS_MODULE=backend.settings.development celery -A backend.celery_app:app worker -l INFO
```

flower monitoring
```python
DJANGO_SETTINGS_MODULE=backend.settings.development celery flower -A backend.celery_app:app --address=127.0.0.1 --port=5555
```

celery beat process
```python
DJANGO_SETTINGS_MODULE=backend.settings.development \
    celery \
    --app=backend.celery_app:app \
    beat \
    --loglevel=INFO
```
