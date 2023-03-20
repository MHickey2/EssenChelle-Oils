from django.shortcuts import render

# Create your views here.


def about(request):
    """ A view to return the about page """

    return render(request, 'story/about.html')


def ourproducts(request):
    """ A view to return the ourproducts page """

    return render(request, 'story/ourproducts.html')


def faq(request):
    """ A view to return the ourproducts page """

    return render(request, 'story/faq.html')
