from math import e
from turtle import title
from typing import Required
from urllib import request
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label='Descripción de la tarea', widget=forms.Textarea, required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
