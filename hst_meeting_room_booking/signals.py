from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Booking
from django.utils import timezone

@receiver(pre_save, sender=Booking)
def check_booking_status(sender, instance, **kwargs):
    if instance.to_date < timezone.now().date():
        instance.is_active = False
    else:
        instance.is_active = True