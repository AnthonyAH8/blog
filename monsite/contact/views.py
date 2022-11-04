from django.http import HttpResponse
from django.shortcuts import render

from .models.contact import Contact

# Retourne la liste des contacts
def contact_list(request):
    contacts = Contact.get_all_contacts()
    print(len(contacts))
    return render(request, 'contact/contact-list.html')

def contact_detail(request):
    return HttpResponse("Liste des contacts")

def contact_new(request):
    return HttpResponse("Liste des contacts")

def contact_edit(request):
    return HttpResponse("Liste des contacts")

def contact_delete(request):
    return HttpResponse("Liste des contacts")
