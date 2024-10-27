from django.shortcuts import render
from Contact.models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST('number')
        description = request.POST('description')
        feedback=Contact.objects.create(fname = fname,email=email, number=number , description=description)
        feedback.save()

    return render(request , 'Contact.html')

def Contacts(request):
    return render(request , "Contact.html")