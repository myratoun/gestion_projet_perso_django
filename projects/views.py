from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Hello World !</h1>")


def login(request):
    return render(request, 'projects/login.html')


class CustomLogoutView(LogoutView):
    template_name = 'projects/logout.html'
    next_page = 'projects:login-page'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
