from django.shortcuts import render
from django.views import generic
from .models import * 

class Playerviev(generic.ListView):
    model= Player
    template_name='zawodnik.html'
    def get_queryset(self): 
        return Player.objects.all() #wyrzuca wszystkie obiekty dla zawodników
# Create your views here.
