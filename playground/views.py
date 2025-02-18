from django.shortcuts import render
from django.http import HttpResponse  # Sax

def say_hello(request):
    return render(request, 'hello.html')
