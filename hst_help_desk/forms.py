from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['issue', 'issue_types', 'issue_detail', 'image']
        
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['issue'].widget.attrs['placeholder'] = 'Enter your issue'
        self.fields['issue_detail'].widget.attrs['placeholder'] = 'Enter your issue in detail'
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'