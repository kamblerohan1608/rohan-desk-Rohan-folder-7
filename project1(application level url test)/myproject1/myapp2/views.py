from django.shortcuts import render,HttpResponse

# Create your views here.

def contacts(request):
    return HttpResponse('<h1>Welcome to Contact Page</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')