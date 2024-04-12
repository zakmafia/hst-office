# tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Booking

@shared_task
def check_booking_status():
    print('Running.....')
    current_date = timezone.now().date()
    bookings_to_update = Booking.objects.filter(to_date__lt=current_date)
    for booking in bookings_to_update:
        booking.is_active = False  # Assuming is_active should be False for expired bookings
        booking.save()
    return 'Status Updated'

