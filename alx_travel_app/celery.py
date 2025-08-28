from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Point Celery to Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

app = Celery("alx_travel_app")

# Read Celery settings from Django with the CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py files in installed apps
app.autodiscover_tasks()

