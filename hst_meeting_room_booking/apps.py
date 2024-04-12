from django.apps import AppConfig


class HstMeetingRoomBookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hst_meeting_room_booking'
    
    def ready(self):
        from . import signals
        from . import tasks
