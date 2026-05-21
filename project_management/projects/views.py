from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Project, Task
from.forms import TaskForm, AssignForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.admin.widgets import AdminDateWidget
from django_htmx.http import trigger_client_event

def responsibility_modal(request, id):
    task = Task.objects.filter(id=id)
    form = AssignForm
    
    if request.method == "POST":
        form = AssignForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('task-detail', pk=id)
        
    context = {'task': task, 'form': form}
    response = render(request, "responsibility-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

class TaskListView(ListView):
   model = Task
   template_name = 'tasks.html'

# class ProjectListView(ListView):
#     model = Planning
#     template_name = 'projects.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = [
                "name",
                "title",
                "print_number",
                "isbn",
                "author_surname",
                "author_first_names",
                "series_name",
                "fonds",
                "description",
                "owner"
            ]
    template_name = 'create-project.html'
    success_url = reverse_lazy('projects')

class ProjectCreatePlanningView(UpdateView):
    model = Project
    fields = [
                "files_due",
                "CB_delivery_due",
                "publishing_date"
            ]
    template_name = 'create-planning.html'
    success_url = reverse_lazy('projects')

    def get_form(self, form_class=None):
        form = super(ProjectCreatePlanningView, self).get_form(form_class)
        form.fields['files_due'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['CB_delivery_due'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['publishing_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The planning was created successfully.")
        return super(ProjectCreatePlanningView ,self).form_valid(form)
    
class ProjectCreateProductionDetailsView(CreateView):
    model = Project
    fields = [
                "project",
                "binding",
                "format",
                "paper_type",
                "print_run",
                "printer",
                "endpaper",
                "cover_material",
                "cover_decoration",
                "print",
                "head_and_tail",
                "reading_ribbon",
                "dust_jacket",
                "extras"
            ]
    template_name = 'create-production-details.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The production details were created successfully.")
        return super(ProjectCreateProductionDetailsView ,self).form_valid(form)

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projectList(request):
    projects = Project.objects.all()
    # planning = Planning.objects.all()
    print("projects:", projects.values('name', 'print_number', 'files_due', 'CB_delivery_due', 'publishing_date'))
    context = {'projects':projects}
    return render(request, 'projects.html', context)


def projectDetail(request,pk):
    project = get_object_or_404(Project, id=pk)
    project_tasks = project.task_set.all()

    context = {'project':project,'project_tasks':project_tasks}
    return render(request, 'project-detail.html', context)

# def taskList(request):
#     user_tasks =Task.objects.filter(assignee=request.user)
#     # tasks = Task.objects.filter(assignee=None)

#     context = {'tasks':user_tasks,'user_tasks':user_tasks}
#     return render(request, 'tasks.html', context)

def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task': task}
    return render(request, 'task-detail.html', context)

def taskCreate(request):
   form = TaskForm
   if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
           form.save() 
           return redirect('tasks')  

   context = {'form':form}
   return render(request, 'task-create.html', context)

def addProject(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')  
        owner = data.get('owner')

        Project.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            owner=request.user
        )
        return redirect('/')

    queryset = Project.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'projects': queryset}
    return render(request, 'projects.html', context)

# def create_project(request):
#     fields = Planning._meta.get_fields()
#     print("fields:", fields)
#     return render(request, 'create-project.html')


def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('/')


def update_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        project.name = name
        project.description = description
        project.save()  
        return redirect('/')

    context = {'project': project}
    return render(request, 'update_project.html', context)

# def add_production_details(request, id):
#     project = get_object_or_404(Project, id=id)
#     if request.method == 'POST':
#         data = request.POST
#         binding = data.get('binding')
#         format = data.get('format')
#         paper_type = data.get('paper_type')
#         print_run = data.get('print_run')
#         printer = data.get('printer')
#         endpaper = data.get('endpaper')
#         cover_material = data.get('cover_material')
#         cover_decoration = data.get('cover_decoration')
#         print = data.get('print')
#         head_and_tail = data.get('head_and_tail')
#         reading_ribbon = data.get('reading_ribbon')
#         dust_jacket = data.get('dust_jacket')
#         extras = data.get('extras')

#         ProductionDetails.objects.create(
#             project=project,
#             binding=binding,
#             format=format,
#             paper_type=paper_type,
#             print_run=print_run,
#             printer=printer,
#             endpaper=endpaper,
#             cover_material=cover_material,
#             cover_decoration=cover_decoration,
#             print=print,
#             head_and_tail=head_and_tail,
#             reading_ribbon=reading_ribbon,
#             dust_jacket=dust_jacket,
#             extras=extras
#         )
#         return redirect('/')

#     context = {'project': project}
#     return render(request, 'add_production_details.html', context)

# def delete_production_details(request, id):
#     production_details = get_object_or_404(ProductionDetails, id=id)
#     production_details.delete()
#     return redirect('/')

# def update_production_details(request, id):
#     production_details = get_object_or_404(ProductionDetails, id=id)
#     if request.method == 'POST':
#         data = request.POST
#         production_details.binding = data.get('binding')
#         production_details.format = data.get('format')
#         production_details.paper_type = data.get('paper_type')
#         production_details.print_run = data.get('print_run')
#         production_details.printer = data.get('printer')
#         production_details.endpaper = data.get('endpaper')
#         production_details.cover_material = data.get('cover_material')
#         production_details.cover_decoration = data.get('cover_decoration')
#         production_details.print = data.get('print')
#         production_details.head_and_tail = data.get('head_and_tail')
#         production_details.reading_ribbon = data.get('reading_ribbon')
#         production_details.dust_jacket = data.get('dust_jacket')
#         production_details.extras = data.get('extras')

#         production_details.save()  
#         return redirect('/')

#     context = {'production_details': production_details}
#     return render(request, 'update_production_details.html', context)

