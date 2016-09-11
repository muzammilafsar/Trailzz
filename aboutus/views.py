#from django.shortcuts import render
from django.views import generic
from .models import About

class Aboutus(generic.ListView):
    template_name = 'movie/about.html'

    def get_queryset(self):
        return About.objects.all()
