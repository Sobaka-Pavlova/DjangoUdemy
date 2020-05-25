from django.shortcuts import render
from djnago.http import HttpResponse


def index(request):
    return HttpResponse('<h1>HelloWorld</h1>')
