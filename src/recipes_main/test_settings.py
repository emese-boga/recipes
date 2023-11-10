from .settings import *
from uuid import uuid4


SECRET_KEY = str(uuid4())
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "recipes_test_db",
    }
}
WHITENOISE_AUTOREFRESH = True
