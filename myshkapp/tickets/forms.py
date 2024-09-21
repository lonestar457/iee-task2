from django import forms
from .models import ticket

class CreateTicketForm(forms.ModelForm):
    class Meta :
        model = ticket
        fields =['title','discription']


class UpdateTicketForm(forms.ModelForm):
    class Meta :
        model = ticket
        fields =['title','discription']