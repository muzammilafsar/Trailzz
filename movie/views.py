from django.views import generic
from .models import Movie_Details
# Create your views here.

class Home(generic.ListView):
    template_name = 'movie/home.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Movie_Details.objects.all()[::-1]

class Detail(generic.DetailView):
    model = Movie_Details
    template_name = 'movie/detail.html'