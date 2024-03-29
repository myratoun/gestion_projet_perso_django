from django.urls import path
from projects.views import add_project, add_tache, update_tache

app_name = "projects"

urlpatterns = [
                  path('add_project/', add_project, name='add-project'),
                  path('update_tache/<int:tache_id>', update_tache, name='update-tache'),
                  path('add_tache/<int:project_id>/', add_tache, name='add-tache'),
              ]

