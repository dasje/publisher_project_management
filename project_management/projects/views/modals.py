from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy

from ..tables import TaskListTable
from ..models import Project, Task, PaperbackProject, HardbackProject, BoxedProject
from..forms import ProjectDescriptionForm, TaskDescriptionForm, TaskForm, AssignForm, TaskStatusForm, TaskTitleForm, ProjectDetailsForm, ProjectPlanningForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.admin.widgets import AdminDateWidget
from django_htmx.http import trigger_client_event
from django_table_sort.table import TableSort
from django_tables2 import SingleTableView

from django.shortcuts import get_object_or_404, redirect, render


def project_planning_modal(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        form = ProjectPlanningForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('project-detail', pk=id)

    else:
        form = ProjectPlanningForm(instance=project)

    context = {
        'project': project,
        'form': form,
        'id': id
    }

    response = render(request, "project-planning-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def project_details_modal(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        form = ProjectDetailsForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('project-detail', pk=id)

    else:
        form = ProjectDetailsForm(instance=project)

    context = {
        'project': project,
        'form': form,
        'id': id
    }

    response = render(request, "project-details-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def project_description_modal(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        form = ProjectDescriptionForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('project-detail', pk=id)

    else:
        form = ProjectDescriptionForm(instance=project)

    context = {
        'project': project,
        'form': form,
        'id': id
    }

    response = render(request, "project-description-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def task_status_modal(request, id):
    task = get_object_or_404(Task, id=id)
    print(request.META)

    if request.method == "POST":
        form = TaskStatusForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            # Return to last page. Previous page needs next parameter in query string for this to work, e.g. ?next=/tasks
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)

    else:
        form = TaskStatusForm(instance=task)

    context = {
        'task': task,
        'form': form,
        'id': id
    }

    response = render(request, "task-status-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def task_title_modal(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskTitleForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=id)

    else:
        form = TaskTitleForm(instance=task)

    context = {
        'task': task,
        'form': form,
        'id': id
    }

    response = render(request, "task-title-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def task_description_modal(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskDescriptionForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=id)

    else:
        form = TaskDescriptionForm(instance=task)

    context = {
        'task': task,
        'form': form,
        'id': id
    }

    response = render(request, "task-description-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

def responsibility_modal(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = AssignForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=id)

    else:
        form = AssignForm(instance=task)

    context = {
        'task': task,
        'form': form,
        'id': id
    }

    response = render(request, "responsibility-modal.html", context)
    return trigger_client_event(response, "modal:show", after="swap")

