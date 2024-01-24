from django.shortcuts import render
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
@login_required()
def home(request):
    return render(request, 'projects/index.html')


def login(request):
    return render(request, 'projects/login.html')


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("Formulaire valide !")
            project = form.save()
            return JsonResponse({'status': 'success', 'project_id': project.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ProjectForm()

    return render(request, 'projects/index.html', {'form': form}),
