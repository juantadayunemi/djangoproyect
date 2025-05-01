from math import e
from turtle import title
from typing import Required
from urllib import request
from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label='Descripción de la tarea', widget=forms.Textarea, required=False)

class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        labels = {
            'name': "Nombre del proyecto"
        }