from .models import Booking
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

def is_booking_valid(booking, room):
    conflicting_bookings = Booking.objects.filter(
        Q(room=room),
        (
            Q(from_date__lte=booking.from_date, to_date__gte=booking.from_date) |
            Q(from_date__lte=booking.to_date, to_date__gte=booking.to_date) |
            Q(from_date__gte=booking.from_date, to_date__lte=booking.to_date)
        ),
        (
            Q(from_time__lte=booking.from_time, to_time__gte=booking.from_time) |
            Q(from_time__lte=booking.to_time, to_time__gte=booking.to_time) |
            Q(from_time__gte=booking.from_time, to_time__lte=booking.to_time)
        )
    )
    return not conflicting_bookings.exists()

def send_booking_email(request, booking):
    current_site = get_current_site(request)
    mail_subject = 'You have Booked a Meeting Room'
    message = render_to_string('bookings/emails/booking_email.html', {
        'user': request.user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
        'token': default_token_generator.make_token(request.user),
        'booking_time_from': booking.from_time,
        'booking_time_to': booking.to_time,
        'booking_date_from': booking.from_date,
        'booking_date_to': booking.to_date,
        'name': booking.name,
        'description': booking.description,
        'booking_id': urlsafe_base64_encode(force_bytes(booking.id)),
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
    
def admin_send_cancellation_email(admin_user, booking_info, reason):
    mail_subject = 'Meeting Room Booking Cancellation'
    message = render_to_string('bookings/emails/admin_cancellation_booking.html', {
        'booking_person_name': booking_info.booking_person.first_name,
        'name': booking_info.name,
        'booking_date_from': booking_info.from_date,
        'booking_date_to': booking_info.to_date,
        'booking_time_from': booking_info.from_time,
        'booking_time_to': booking_info.to_time,
        'admin_name': admin_user.username,
        'reason': reason
    })
    to_email = booking_info.booking_person.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()