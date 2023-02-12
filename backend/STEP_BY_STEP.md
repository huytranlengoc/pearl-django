## Start new django project

```python
django-admin startproject backend
```

## Update `.gitgnore` followed by:

```
https://www.toptal.com/developers/gitignore/api/python,django
```

## Splitting settings environments

Move `backend/settings.py` to `backend/settings/base.py`
Create `backend/settings/{__init__,base,development,staging,production}.py`

## Customize user model

```python
AUTH_USER_MODEL = "accounts.User"
```

## Create base model for common fields

```python
created_at = models.DateTimeField(auto_now_add=True, editable=False)
updated_at = models.DateTimeField(auto_now=True)
created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    default=None,
    blank=True,
    on_delete=models.SET_NULL,
)
updated_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    default=None,
    blank=True,
    on_delete=models.SET_NULL,
)
```

## Setup Celery app
* Create `backend/celery_app.py`

```python
from celery import Celery
from django.conf import settings

app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

* Declare on `backend/__init__.py`

```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```

* Add celery settings to django

```python
REDIS_SERVICE_HOST = os.environ.get("REDIS_SERVICE_HOST", "localhost")
REDIS_PORT = 6379
BROKER_PORT = 1
RESULTS_PORT = 2

CELERY_BROKER_URL = f"redis://{REDIS_SERVICE_HOST}:{REDIS_PORT}/{BROKER_PORT}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_SERVICE_HOST}:{REDIS_PORT}/{RESULTS_PORT}"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
```
