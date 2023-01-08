from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome To Home Page</h1>')

def services(request):
    return HttpResponse('<h1>Welcome To Services Page</h1>')