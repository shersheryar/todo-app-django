from django.shortcuts import render, redirect   
# from django.http import HttpResponse
from . models import Task
from . forms import TaskForm

# Create your views here.

def  index(requrest):
    form = TaskForm()
    tasks = Task.objects.all()
    
    if requrest.method == 'POST':
        form = TaskForm(requrest.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, "TaskForm": form}
    return render(requrest, 'tasks.html', context)
    # return render(requrest, 'tasks.html')