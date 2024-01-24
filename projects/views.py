from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def home(request):
    return render(request, 'projects/index.html')


def login(request):
    return render(request, 'projects/login.html')
