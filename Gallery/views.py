from django.shortcuts import render
from Home.models import Photographs
# Create your views here.
def gallery(request, category):
    pics = Photographs.objects.filter(category=category).all()
    return render(request, 'gallery.html', {'pics':pics,
                                            'c':category})