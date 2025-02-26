from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  index(requrest):
    return render(requrest, 'tasks.html')