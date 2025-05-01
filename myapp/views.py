from queue import PriorityQueue
import re
from urllib import request
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    title = "Django course!!."
    return render(request, 'index.html', {'title':title})

def about(request):
    username = "juan"
    return render(request,"about.html", {'username': username})

def hello(request, id):
    return HttpResponse("<h1>Hello %s</h>" % id)


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {'projects':projects})

def tasks(request):
    try:
        tasks = Task.objects.all()
        return render(request, 'tasks/task.html', {'tasks': tasks})
    except Task.DoesNotExist:
        raise Http404("La tarea no existe   ")
    

def create_task(request):
    if request.method == 'GET':
        form = CreateNewTask()   # instancia
        return render(request, 'tasks/create_task.html', {'form': form})
    
    # POST
    form = CreateNewTask(request.POST)
    if form.is_valid():

        # usa cleaned_data, aquí description coincide con tu forms.CharField

        Task.objects.create(
            title       = form.cleaned_data['title'],
            description = form.cleaned_data['description'],
            project_id  = 1
        )

        return redirect('tasks')  # usa nombre de URL en lugar de literal
    # si no es válido, vuelve a mostrar el formulario con errores
    return render(request, 'create_task.html', {'form': form})


def create_project(request):

    if request.method == 'GET':
        form = CreateNewProject()
        return render(request, 'projects/create_project.html', {'form': form})
    
    # POST request
    form = CreateNewProject(request.POST)
    if form.is_valid():
        # ✅ Correct: Create a Project (not a Task)
        Project.objects.create(
            name=form.cleaned_data['name']
        )
        return redirect('projects')
    
    # If form is invalid, show errors
    return render(request, 'projects/create_project.html', {'form': form})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks  = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html' , {
        'project' : project,
        'tasks': tasks
        })

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = CreateNewProject(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', id=project.id)
    else:
        form = CreateNewProject(instance=project)
    return render(request, 'projects/edit.html', {'form': form, 'project': project})
