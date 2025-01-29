import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

app.conf.beat_schedule = {
    "run-every-day": {
        "task": "dashboard.tasks.generate_ai_feedback",
        "schedule": crontab(hour=0, minute=0),
    },
}

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
