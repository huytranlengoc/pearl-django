# Backend structure
```python
├── core
│   ├── settings # environment settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── staging.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   │── common # common settings
│   │   ├── models
│   │   │   └── base.py # common fields
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── managers
│   │   │   └── user.py
│   │   ├── migrations
│   │   ├── models
│   │   │   └── user.py # customize user
│   │   ├── tests.py
│   │   └── views.py
│   ├── api
│   │   └── ... # for api
│   └──── ... # for another apps
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   ├── production.txt
│   └── test.txt
│── requirements.txt
├── manage.py
└── README.md
```

# Configuration

# How to runz

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
