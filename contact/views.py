from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.


def contact(request):
    """ A view to show the contact form for the user """

    # template = "contact/contact.html"
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            email_subject = f'New contact {form.cleaned_data["email_address"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, '', ['michellehickey2@yahoo.ie'],)
            messages.success(request, 'Your message has been sent!')
            return render(request, 'contact/success.html')
           
        else:
            # Form is invalid. Render the form again with error messages.
            messages.error(request, 'Invalid form submission.')
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
