from django.shortcuts import render
from .models import Photographs

# Create your views here.
def index(request):
    pics = Photographs.objects.all()
    return render(request, 'index.html', {'pics':pics})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')