from django.shortcuts import render
from django.views import generic
from .models import Home

class Homeview(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'object_list'

    # Game_carousel.objects.all()
    def get_queryset(self):
        return Home.objects.all()
