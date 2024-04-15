from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('manage-rooms/', views.manage_rooms, name='manage_rooms'),
    path('room-info/<str:room_id>/', views.view_room_information, name='room_info'),
    
    path('cancel_booking_validate/<uidb64>/<token>/<booking_id>/', views.cancel_booking_validate, name='cancel_booking_validate'),
    path('cancel-booking-from-email/', views.cancel_booking_view_from_email, name='cancel_booking_view_from_email')
]
