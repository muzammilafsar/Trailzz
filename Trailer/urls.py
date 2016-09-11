
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('home.urls') ,name='home'),
    url(r'^home/',include('home.urls') ,name='home'),
    url(r'^movie/',include('movie.urls') ,name='movie'),
    url(r'^game/',include('game.urls') ,name='game'),
    url(r'^aboutus/',include('aboutus.urls') ,name='game'),
]
