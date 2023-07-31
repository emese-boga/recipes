"""
WSGI config for vod_import_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipes_main.settings")

wsgi_application = get_wsgi_application()
application = WhiteNoise(wsgi_application, root=settings.STATIC_ROOT)
