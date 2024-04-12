from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Room
from .forms import BookingForm, RoomForm
from .utils import is_booking_valid, send_booking_email

@login_required(login_url='login')
def bookings(request):
    rooms = Room.objects.all()
    bookings = Booking.objects.filter(is_active=True)
    context = {
        'title_name': 'Bookings',
        'rooms': rooms,
        'bookings': bookings
    }
    return render(request, 'hst_meeting_room_booking/bookings.html', context)

@login_required(login_url='login')
def my_bookings(request):
    my_bookings = Booking.objects.filter(booking_person=request.user, is_active=True).order_by('-created_on')
    my_bookings_history = Booking.objects.filter(booking_person=request.user).order_by('-created_on')
    if 'cancel_my_booking' in request.POST:
           booking_id = request.POST.get('my_booking_id')
           booking = get_object_or_404(Booking, id=booking_id)
           booking.delete()
    if 'remove_my_booking' in request.POST:
           booking_id = request.POST.get('my_booking_id')
           booking = get_object_or_404(Booking, id=booking_id)
           booking.delete()
    context = {
        'title_name': 'My Bookings',
        'my_bookings': my_bookings,
        'my_bookings_history': my_bookings_history
    }
    return render(request, 'hst_meeting_room_booking/my_bookings.html', context)

@login_required(login_url='login')
def manage_rooms(request):
    rooms = Room.objects.all()
    form = RoomForm()
    if 'add_a_room' in request.POST:
        form = RoomForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'You have added a Room')
                return redirect('manage_rooms')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    if 'delete_a_room' in request.POST:
        room_id = request.POST.get('room_id')
        room = get_object_or_404(Room, id=room_id)
        room.delete()
        
    if 'edit_a_room' in request.POST:
        room_id = request.POST.get('room_id')
        room = get_object_or_404(Room, id=room_id)
        room.name = request.POST.get('room_name')
        room.address = request.POST.get('room_address')
        room.save()
        
    
    context = {
        'title_name': 'Manage Rooms',
        'rooms': rooms,
        'form': form
    }
    return render(request, 'hst_meeting_room_booking/manage_rooms.html', context)

@login_required(login_url='login')
def view_room_information(request, room_id):
    form = BookingForm()
    booking_person = request.user
    room = Room.objects.get(id=room_id)
    booking_info = Booking.objects.filter(room=room, is_active=True).order_by('-created_on')
    
    if 'book' in request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if is_booking_valid(booking, room):
                booking.booking_person = booking_person
                booking.room = room
                send_booking_email(request, booking)
                booking.save()
                messages.success(request, 'You have booked a Meeting Room')
                return HttpResponseRedirect('/room-booking/room-info/' + str(room_id))
            else:
                messages.error(request, 'Booking made with the same time and date')
                return HttpResponseRedirect('/room-booking/room-info/' + str(room_id))  
            
    if 'cancel_booking' in request.POST:
           booking_id = request.POST.get('booking_id')
           reason = request.POST.get('reason')
           booking = get_object_or_404(Booking, id=booking_id)
           booking.delete()
    
    context = {
        'type': 'room_type',
        'title_name': room.name,
        'room': room,
        'booking_info': booking_info,
        'form': form
    }
    return render(request, 'hst_meeting_room_booking/room_info.html', context)

        
    
