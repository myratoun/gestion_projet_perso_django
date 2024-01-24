from django.urls import path
from projects.views import add_project

app_name = "projects"

urlpatterns = [
                  path('add_project/', add_project, name='add-project'),
              ]
