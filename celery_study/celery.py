from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_study.settings')

app = Celery('celery_study')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#celery will automatically discover tasks in all registered apps
#celert beat settings
app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')