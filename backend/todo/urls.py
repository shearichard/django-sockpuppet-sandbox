from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import todo.views.todo_reflex


from . import viewsNOTTHEDIRECTORY as viewsNTD


urlpatterns = [
    path('', viewsNTD.index, name='index'),
    path('todo/', todo.views.todo_reflex.todoreflexview, name='todo'),
] + staticfiles_urlpatterns()
