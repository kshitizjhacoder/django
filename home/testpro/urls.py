from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('pnrsearch', views.pnrsearch, name='pnrsearch'),
    path('timesearch', views.timesearch, name='timesearch'),
    path('cancel', views.cancel, name='cancel'),
    path('cancel_this/<id>', views.cancel_this, name='cancel'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path(r'^details/<int:id>/$', views.details, name='details'),
    path('reservation', views.reservation, name='reservation')

]
