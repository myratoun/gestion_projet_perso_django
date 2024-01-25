from django import forms
from .models import Project, Tache


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ["project", "number_order", "description", "date_end"]
