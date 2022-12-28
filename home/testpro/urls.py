from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('pnrsearch', views.pnrsearch, name='pnrsearch'),
    path('timesearch', views.timesearch, name='timesearch'),

    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path(r'^details/<int:id>/$', views.details, name='details')
]
