from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is first app/ Course Page. ")
def home(request):
    return HttpResponse("This is first app Page. ")

def about(request):
    return HttpResponse("This is first app/ About Page. ")

