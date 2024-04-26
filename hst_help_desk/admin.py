from django.contrib import admin
from .models import Ticket, KnowledgeBase

class TicketAdmin(admin.ModelAdmin):
    list_display = ('issue', 'issue_types', 'requester', 'status', 'created_on')
    list_filter = ('status', 'issue_types', 'created_on')
    search_fields = ('issue', 'issue_detail', 'requester__username')
    readonly_fields = ('id', 'created_on')
    fieldsets = (
        (None, {
            'fields': ('id', 'issue', 'issue_types', 'issue_detail', 'image')
        }),
        ('Requester Information', {
            'fields': ('requester',)
        }),
        ('Ticket Status', {
            'fields': ('status', 'checked', 'created_on'),
            'classes': ('collapse',)  # Hide this fieldset by default
        }),
    )
    ordering = ('-created_on',)  # Display tickets ordered by created_on in descending order

class KnowledgeBaseAdmin(admin.ModelAdmin):
    ordering = ('-created_on',)  # Display knowledge base entries ordered by created_on in descending order

admin.site.register(Ticket, TicketAdmin)
admin.site.register(KnowledgeBase, KnowledgeBaseAdmin)
