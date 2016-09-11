from django.conf.urls import url
from . import views

app_name='movie'
urlpatterns = [

    url(r'^$',views.Home.as_view() ,name='home'),
    url(r'^(?P<pk>[0-9]+)/$',views.Detail.as_view(),name='detail')
]
