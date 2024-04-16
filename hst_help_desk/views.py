from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm

@login_required(login_url='login')
def help_desk(request):
    context = {
        'title_name': 'Help Desk'
    }
    return render(request, 'hst_help_desk/help_desk.html', context)

@login_required(login_url='login')
def my_requests(request):
    form = TicketForm()
    tickets = Ticket.objects.filter(requester=request.user)
    if 'create_a_ticket' in request.POST:
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have created a new Ticket')
            return redirect('my_requests')
    context = {
        'title_name': 'My Requests',
        'tickets': tickets,
        'form': form
    }
    return render(request, 'hst_help_desk/my_requests.html', context)

@login_required(login_url='login')
def knowledge_base(request):
    context = {
        'title_name': 'Knowledge Base'
    }
    return render(request, 'hst_help_desk/knowledge_base.html', context)
