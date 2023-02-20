from django import forms
from .models import Contact
from django.forms import ModelForm, TextInput

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# Create your forms here.


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'message')

    widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email_address': forms.TextInput(attrs={'placeholder': 'Enter your email address'}),
            'message': SummernoteWidget(),
    }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def success(request):
        return render(request, "contact/success.html")
    