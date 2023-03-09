from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse('<marquee><h1>Today is First Django Practice the project</h1></marquee>')

def hari(request):
    return HttpResponse('<h1>I Want Job is Important for Life</h1>')
