from django.conf.urls import url
from aboutus import views

app_name='aboutus'
urlpatterns = [

    url(r'^$',views.Aboutus.as_view() ,name='home'),

]
