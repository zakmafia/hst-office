from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('manage-rooms/', views.manage_rooms, name='manage_rooms'),
    path('room-info/<str:room_id>/', views.view_room_information, name='room_info'),
]
