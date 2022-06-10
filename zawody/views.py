from django.shortcuts import render
from django.views import generic

from zawody.forms import playerForm
from .models import * 

class Playerviev(generic.ListView):
    model= Player
    template_name='zawodnik.html'#nazwa html
    def get_queryset(self): 
        return Player.objects.all() #wyrzuca wszystkie obiekty dla zawodników

class Competitionviev(generic.ListView):
    model= Competition
    template_name='zawody.html'
    def get_queryset(self): 
        return Competition.objects.all()

class Bikeviev(generic.ListView):
    model= Bike
    template_name='rower.html'
    def get_queryset(self): 
        return Bike.objects.all()

class PlayerDetail(generic.DetailView):
    model=Player
    template_name = 'playerdetail.html'
    slug_field = 'shortcut'
    def list(request, title):
        modes = Player.objects.get(title=title)
        context = {
            'modes' : modes
        }
        return render(request, 'playerdetail.html', context)

def form_view(request):
    form = playerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
        }
    return render(request, "forms.html",context)

