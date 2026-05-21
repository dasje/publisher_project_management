from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5 import bootstrap5
from .models import Task, Project

class TaskForm(ModelForm):
    class Meta:
        model =Task
        fields ='__all__'
        widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }
        
class AssignForm(ModelForm):
    class Meta:
        model = Task
        fields = ['assignee']

