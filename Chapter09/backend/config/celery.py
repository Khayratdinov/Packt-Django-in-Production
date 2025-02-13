import os
from celery import Celery

celery_settings_value = "config.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", celery_settings_value)

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

task = app.task


@app.task(bind=True)
def debug_task(self, data):
    print(data)
