from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Task

tasks = []


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            task = Task(title)
            tasks.append(task)
        return render(request, 'todo/index.html', {'tasks': tasks})


def list_task(request):
    return render(request, 'todo/index.html',{'tasks': tasks})