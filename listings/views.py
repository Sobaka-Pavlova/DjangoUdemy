from django.shortcuts import render

from .models import Listing

def index(request):
    return render(request,'listings/listings.html', {
       'name' : "Brad"


    })


def listing(request):
   return render(request, 'listings/listing.html')


def search(request):
   return render(request, 'listings/search.html')
