import django_tables2 as tables
from .models import Task

class TaskListTable(tables.Table):
    actions = tables.TemplateColumn(
        template_code='''
            <a 
                hx-get="{% url 'task-status-modal' record.id %}?next={{ request.path|urlencode }}"
                hx-swap="beforeend"
                hx-target="body"
                class="btn btn-success">{{ record.status }}</a>
        ''',
        orderable=False,
    )
    details = tables.TemplateColumn(
        template_code='''
            <a href="{% url "task-detail" record.id %}"
               class="btn btn-success">
               Detail/Update
            </a>
        ''',
        orderable=False,
    )

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "assignee", "due_date", "project") 
        sequence = ("title", "assignee", "due_date", "project", "actions", "details")
    