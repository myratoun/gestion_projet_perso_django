from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Hello World !</h1>")


def login(request):
    return render(request, 'projects/login.html')
