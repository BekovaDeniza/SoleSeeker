from django.shortcuts import render
from .models import Sneaker


def home(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'home.html', {'sneakers': sneakers})
