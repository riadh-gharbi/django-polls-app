#url config for polls web app

from django.urls import path

# from this directory
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]

