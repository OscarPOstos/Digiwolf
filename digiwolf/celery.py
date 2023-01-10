from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digiwolf.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('digiwolf', broker='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def add(x, y):
    print(x + y)
