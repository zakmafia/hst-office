from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, KnowledgeBase
from .forms import TicketForm
from .utils import send_ticket_email, paginateTickets, send_ticket_checked_email, send_ticket_status_update_email

@login_required(login_url='login')
def help_desk(request):
    user_requests_counter = Ticket.objects.filter(checked=False).count()
    my_requests_counter = Ticket.objects.filter(requester=request.user, status='in_progress').count()
    context = {
        'title_name': 'Help Desk',
        'user_requests_counter': user_requests_counter,
        'my_requests_counter': my_requests_counter
    }
    return render(request, 'hst_help_desk/help_desk.html', context)

@login_required(login_url='login')
def my_requests(request):
    form = TicketForm()
    tickets = Ticket.objects.filter(requester=request.user, status='in_progress').order_by('-created_on')
    addressed_tickets = Ticket.objects.filter(requester=request.user).exclude(status='in_progress').order_by('-created_on')
    custom_range, addressed_tickets = paginateTickets(request, addressed_tickets, 6)
    if 'create_a_ticket' in request.POST:
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.requester = request.user
            send_ticket_email(request, ticket)
            ticket.save()
            messages.success(request, 'You have created a new Ticket')
            return redirect('my_requests')
    if 'request_status_button' in request.POST:
        ticket_id = request.POST.get('my_ticket_id')
        request_status_value = request.POST.get('request_status_value')
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.status = request_status_value
        send_ticket_status_update_email(request, ticket)
        ticket.save()
        messages.success(request, 'You have updated the status of the Ticket')
        
    context = {
        'title_name': 'My Requests',
        'tickets': tickets,
        'addressed_tickets': addressed_tickets,
        'form': form,
        'custom_range': custom_range,
    }
    return render(request, 'hst_help_desk/my_requests.html', context)

@login_required(login_url='login')
def user_requests(request):
    tickets = Ticket.objects.filter(checked=False).order_by('-created_on')
    checked_tickets= Ticket.objects.filter(checked=True, status='in_progress').order_by('-created_on')
    addressed_tickets = Ticket.objects.filter(checked=True).exclude(status='in_progress').order_by('-created_on')
    custom_range, addressed_tickets = paginateTickets(request, addressed_tickets, 6)
    context = {
        'title_name': 'User Requests',
        'tickets': tickets,
        'checked_tickets': checked_tickets,
        'addressed_tickets': addressed_tickets,
        'custom_range': custom_range,
    }
    
    if 'request_checked' in request.POST:
        ticket_id = request.POST.get('user_ticket_id')
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if ticket.checked == False:
            ticket.checked = True
            print(ticket.checked)
            send_ticket_checked_email(request, ticket)
            ticket.save()
            messages.success(request, 'You have checked the request!')
    return render(request, 'hst_help_desk/user_requests.html', context)

@login_required(login_url='login')
def knowledge_base(request):
    knowledge_bases = KnowledgeBase.objects.all().order_by('-created_on')
    context = {
        'title_name': 'Knowledge Base',
        'knowledge_bases': knowledge_bases
    }
    return render(request, 'hst_help_desk/knowledge_base.html', context)
