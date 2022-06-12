from __future__ import absolute_import

import os

from celery import Celery
from real_estates.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estates.settings.development")

app = Celery("real_estates")

app.config_from_object("real_estatea.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
