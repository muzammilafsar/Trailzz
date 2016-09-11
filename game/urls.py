from django.conf.urls import url
from game import views

app_name='game'
urlpatterns = [

    url(r'^$',views.Home.as_view() ,name='home'),
    url(r'^(?P<pk>[0-9]+)/$',views.Detail.as_view(),name='detail')
]
