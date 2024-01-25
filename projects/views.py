from django.shortcuts import render
from .forms import ProjectForm, TacheForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .models import Project


# Create your views here.
@login_required()
def home(request):
    projects = Project.objects.prefetch_related('tache_set').all()
    return render(request, 'projects/index.html', {'projects': projects})


def login(request):
    return render(request, 'projects/login.html')


def add_project(request):
    submitted = False
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return JsonResponse({'status': 'success', 'project_id': project.id})
            return HttpResponseRedirect("/")
    else:
        form = ProjectForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'projects/add_project_form.html', {'form': form})


def add_tache(request, project_id):
    submitted = False
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TacheForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'projects/add_tache_form.html', {'project': project_id})


def update_tache(request, tache_id):
    return HttpResponseRedirect("/")
