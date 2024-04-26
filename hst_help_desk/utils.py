from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from accounts.models import Account

def send_ticket_email(request, ticket):
    current_site = get_current_site(request)
    requester_subject = 'Your ticket has been submitted'
    requester_message = render_to_string('helpdesk/emails/ticket_email.html', {
        'issue': ticket.issue,
        'issue_types': ticket.issue_types,
        'issue_detail': ticket.issue_detail,
        'requester': ticket.requester,
        'domain': current_site
    })
    
    help_desk_admin_subject = 'A new ticket has been submitted'
    help_desk_admin_message = render_to_string('helpdesk/emails/help_desk_admin_ticket_email.html', {
        'issue': ticket.issue,
        'issue_types': ticket.issue_types,
        'issue_detail': ticket.issue_detail,
        'requester': ticket.requester,
        'domain': current_site
    })
    
    # Send email to the requester
    to_email_requester = request.user.email
    requester_email = EmailMessage(requester_subject, requester_message, to=[to_email_requester])
    requester_email.send()
    
    help_desk_admins = Account.objects.filter(role='help_desk_admin')

    if help_desk_admins.exists():
        # Send email to each help desk admin
        for admin in help_desk_admins:
            to_email_admin = admin.email
            admin_email = EmailMessage(help_desk_admin_subject, help_desk_admin_message, to=[to_email_admin])
            admin_email.send()
            
def send_ticket_status_update_email(request, ticket):
    current_site = get_current_site(request)
    requester_subject = 'You have updated the status of your ticket'
    requester_message = render_to_string('helpdesk/emails/user_addressed_request.html', {
        'issue': ticket.issue,
        'issue_types': ticket.issue_types,
        'issue_detail': ticket.issue_detail,
        'requester': ticket.requester,
        'status': ticket.status,
        'domain': current_site
    })
    
    help_desk_admin_subject = 'The user has given feedback on the ticket you checked'
    help_desk_admin_message = render_to_string('helpdesk/emails/help_desk_admin_user_addressed_request.html', {
        'issue': ticket.issue,
        'issue_types': ticket.issue_types,
        'issue_detail': ticket.issue_detail,
        'requester': ticket.requester,
        'status': ticket.status,
        'domain': current_site
    })
    
    # Send email to the requester
    to_email_requester = request.user.email
    requester_email = EmailMessage(requester_subject, requester_message, to=[to_email_requester])
    requester_email.send()
    
    help_desk_admins = Account.objects.filter(role='help_desk_admin')

    if help_desk_admins.exists():
        # Send email to each help desk admin
        for admin in help_desk_admins:
            to_email_admin = admin.email
            admin_email = EmailMessage(help_desk_admin_subject, help_desk_admin_message, to=[to_email_admin])
            admin_email.send()

def send_ticket_checked_email(request, ticket):
    current_site = get_current_site(request)
    requester_subject = 'Help Desk Admin have checked your ticket'
    requester_message = render_to_string('helpdesk/emails/help_desk_admin_checked_ticket.html', {
        'issue': ticket.issue,
        'issue_types': ticket.issue_types,
        'issue_detail': ticket.issue_detail,
        'requester': ticket.requester,
        'status': ticket.status,
        'domain': current_site
    })
    
    # Send email to the requester
    to_email_requester = ticket.requester.email
    requester_email = EmailMessage(requester_subject, requester_message, to=[to_email_requester])
    requester_email.send()

def paginateTickets(request, tickets, results):
    page = request.GET.get('page')
    paginator = Paginator(tickets, results)
    
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        tickets = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        tickets = paginator.page(page)
    
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
    
    return custom_range, tickets