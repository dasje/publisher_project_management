from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects', views.projectList, name = 'projects'),
    path('projects/<int:pk>', views.projectDetail, name ='project-detail'),
    path('tasks', views.TaskListView.as_view(), name ='tasks'),
    path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
    path('create-project', views.ProjectCreateView.as_view(), name='create-project'),
    path('create-task', views.taskCreate, name ='create-task'),
    path('create-planning', views.ProjectCreatePlanningView.as_view(), name = 'create-planning'),
    path('create-production-details', views.ProjectCreateProductionDetailsView.as_view(), name = 'create-production-details'),
    path("responsibility-modal/<int:id>", views.responsibility_modal, name="responsibility-modal"),
    
]