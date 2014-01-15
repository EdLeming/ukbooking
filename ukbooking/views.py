from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.views import generic
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

import calendar
import datetime
import time

from ukbooking.models import Apartment, Bed, Booking, Visit
#from snolab_booking.forms import VisitForm

def index(request):
    """ Return generic index."""
    return render(request, 'ukbooking/index.html')

class Apartments(generic.ListView):
    model = Apartment
    template_name = "ukbooking/apartments.html"

def apartment(request, apartment_id):
    """ Return apartment information."""
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    try:
        beds = Bed.objects.filter(apartment=apartment_id)
        return render(request, 'ukbooking/apartment.html', {'apartment' : apartment, 'bed_list' : beds})
    except Bed.DoesNotExist:
        return render(request, 'ukbooking/apartment.html', {'apartment' : apartment, 'bed_list' : []})
