from django.db import models
from django.conf import settings
import uuid
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    description = models.TextField(max_length=255, blank=True, null=True)
    booking_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

