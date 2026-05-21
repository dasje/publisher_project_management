from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    # meta details
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    title = models.CharField(max_length=150)
    print_number = models.IntegerField(null=True, blank=True)
    author_surname = models.CharField(max_length=100, null=True, blank=True)
    author_first_names = models.CharField(max_length=100, null=True, blank=True)
    series_name = models.CharField(max_length=100, null=True, blank=True)
    fonds = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # production details
    binding = models.CharField(max_length=100, null=True, blank=True)
    format = models.CharField(max_length=100, null=True, blank=True)
    paper_type = models.CharField(max_length=100, null=True, blank=True)
    print_run = models.IntegerField(null=True, blank=True)
    printer = models.CharField(max_length=100, null=True, blank=True)
    endpaper = models.CharField(max_length=100, null=True, blank=True)
    cover_material = models.CharField(max_length=100, null=True, blank=True)
    cover_decoration = models.CharField(max_length=100, null=True, blank=True)
    print = models.CharField(max_length=100, null=True, blank=True)
    head_and_tail = models.CharField(max_length=100, null=True, blank=True)
    reading_ribbon = models.CharField(max_length=100, null=True, blank=True)
    dust_jacket = models.CharField(max_length=100, null=True, blank=True)
    extras = models.TextField(null=True, blank=True)

    # planning details
    files_due = models.DateField(null=True, blank=True)
    CB_delivery_due = models.DateField(null=True, blank=True)
    publishing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title + '_' + str(self.print_number)
    
    class Meta:
        ordering = ['-date_created'] # Sorts all returned data by date_created

class Task(models.Model):
    TODO="TO DO"
    COMPLETED='COMPLETED'
    INPROGRESS='IN-PROGRESS'
    STATUS_CHOICES = [
        (TODO, 'TO DO'),
        (COMPLETED, 'COMPLETED'),
        (INPROGRESS, 'IN-PROGRESS'),

    ]
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    project = models.ForeignKey(Project,blank=True, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= TODO)

    def __str__(self):
        return self.title