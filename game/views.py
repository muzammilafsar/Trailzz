#from django.shortcuts import render
from django.views import generic
from .models import Game_Details,Game_carousel

class Home(generic.ListView):
    template_name = 'game/home.html'
    context_object_name = 'object_list'
    #Game_carousel.objects.all()
    def get_queryset(self):
        return Game_Details.objects.all()[::-1]

class Detail(generic.DetailView):
    model = Game_Details
    template_name = 'movie/detail.html'
