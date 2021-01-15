from django.shortcuts import render
from django.http import HttpResponse

ATESTVALUE="ATESTVALUE"

def index(request):
    return render(request, 'todo/index.html')
