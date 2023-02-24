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
            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
            # return redirect('success')
            
            send_mail(subject, message, from_email, ['michellehickey2@yahoo.ie'],)

        else:
            form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
