from django.urls import path

from . import viewsNOTTHEDIRECTORY as views

urlpatterns = [
    path('', views.index, name='index'),
]
