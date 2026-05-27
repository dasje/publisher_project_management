from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5 import bootstrap5
from .models import BoxedProject, HardbackProject, PaperbackProject, Task, Project


class PaperbackProjectDetailSpecificationForm(ModelForm):
    class Meta:
        model = PaperbackProject
        fields ='__all__'

class HardbackProjectDetailSpecificationForm(ModelForm):
    class Meta:
        model = HardbackProject
        fields ='__all__'
        
class BoxedProjectDetailSpecificationForm(ModelForm):
    class Meta:
        model = BoxedProject
        fields ='__all__'
        
class TaskForm(ModelForm):
    class Meta:
        model =Task
        fields ='__all__'
        widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }
        
class PaperbackProjectForm(ModelForm):
    class Meta:
        model = PaperbackProject
        fields ='__all__'
        widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }
        
class HardbackProjectForm(ModelForm):
    class Meta:
        model = HardbackProject
        fields ='__all__'
        widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }
        

class BoxedProjectForm(ModelForm):
    class Meta:
        model = BoxedProject
        fields ='__all__'
        widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }
        
class AssignForm(ModelForm):
    class Meta:
        model = Task
        fields = ['assignee']

class TaskStatusForm(ModelForm):
    class Meta:
        model = Task
        fields = ['status']

class TaskDescriptionForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class TaskTitleForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class ProjectDescriptionForm(ModelForm):
    class Meta:
        model = Project
        fields = ['description']

class ProjectDetailsForm(ModelForm):
    class Meta:
        model = Project
        fields = ['isbn', 'title', 'print_number', 'author_surname','author_first_names','series_name','fonds','offer_name','owner']

class ProjectPlanningForm(ModelForm):
    class Meta:
        model = Project
        fields = ['manuscript_due', 'translation_due', 'pre_press_due', 'print_ready_manuscript_due', 'cover_and_artwork_due', 'files_due', 'CB_delivery_due', 'publishing_date']

        widgets = {'manuscript_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'translation_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'pre_press_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'print_ready_manuscript_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'cover_and_artwork_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'files_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'CB_delivery_due': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            'publishing_date': DateInput( format=('%Y-%m-%d'),
            attrs={'type': 'date' }),
            }