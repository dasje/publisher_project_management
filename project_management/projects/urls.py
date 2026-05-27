from django.urls import path
from .views import views
from .views import modals

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projects', views.projectList, name = 'projects'),
    path('projects/<int:pk>', views.projectDetail, name ='project-detail'),
    path('tasks', views.TaskListView.as_view(), name ='tasks'),
    path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
    path('create-project', views.projectCreateNew, name ='create-project'),
    path('create-paperback-project', views.PaperbackProjectCreateView.as_view(), name='create-paperback-project'),
    path('create-hardback-project', views.HardbackProjectCreateView.as_view(), name='create-hardback-project'),
    path('create-boxed-project', views.BoxedProjectCreateView.as_view(), name='create-boxed-project'),
    path('create-task', views.taskCreate, name ='create-task'),
    path('create-planning', views.ProjectCreatePlanningView.as_view(), name = 'create-planning'),
    path('create-production-details', views.ProjectCreateProductionDetailsView.as_view(), name = 'create-production-details'),
    path("responsibility-modal/<int:id>", modals.responsibility_modal, name="responsibility-modal"),
    path("task-description-modal/<int:id>", modals.task_description_modal, name="task-description-modal"),
    path("task-title-modal/<int:id>", modals.task_title_modal, name="task-title-modal"),
    path("task-status-modal/<int:id>", modals.task_status_modal, name="task-status-modal"),
    path("project-description-modal/<int:id>", modals.project_description_modal, name="project-description-modal"),
    path("project-details-modal/<int:id>", modals.project_details_modal, name="project-details-modal"),
    path("project-planning-modal/<int:id>", modals.project_planning_modal, name="project-planning-modal"),
    
]