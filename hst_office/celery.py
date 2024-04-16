# path/to/your/proj/src/cfehome/celery.py
import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hst_office.settings')

app = Celery('hst_office')

app.conf.beat_schedule = {
    'check_booking_status': {
        'task': 'hst_meeting_room_booking.tasks.check_booking_status',  # Task name
        'schedule': crontab(hour="*/12"),  # Run every 12 hours
    },
}

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'
app.autodiscover_tasks()

# We used CELERY_BROKER_URL in settings.py instead of:
# app.conf.broker_url = ''

# We used CELERY_BEAT_SCHEDULER in settings.py instead of:
# app.conf.beat_scheduler = ''django_celery_beat.schedulers.DatabaseScheduler'
