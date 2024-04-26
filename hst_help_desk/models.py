from django.db import models
import uuid
import os
from django.conf import settings
    
class Ticket(models.Model):
    PRIORITY_TYPES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    ISSUE_TYPES = (
        ('software', 'Software'),
        ('hardware', 'Hardware'),
        ('other', 'Other')
    )
    STATUS_TYPES = (
        ('in_progress', 'In-Progress'),
        ('solved', 'Solved'),
        ('not_solved', 'Not-Solved')
    )
    issue = models.CharField(max_length=100)
    issue_types = models.CharField(
        max_length=200, choices=ISSUE_TYPES)
    issue_detail = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='help_desk')
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, choices=STATUS_TYPES, null=True, blank=True, default='in_progress')
    checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return f'{self.requester} - {self.issue}'

class KnowledgeBase(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    name = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(KnowledgeBase, self).delete(*args, **kwargs)