from django.shortcuts import render

# Add essa classe HttpResponse
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def contact(request):
	return render(request,'contact.html')
