from django import forms
from .models import Contact
from django.forms import ModelForm, TextInput

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# Create your forms here.


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'subject', 'message')

    widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),  # noqa
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),  # noqa
            'email_address': forms.TextInput(attrs={'placeholder': 'Enter your email address', 'class': 'form-control'}),  # noqa
            'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject', 'class': 'form-control'}),  # noqa
            'message': SummernoteWidget(),
    }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def success(request):
        return render(request, "contact/success.html")
