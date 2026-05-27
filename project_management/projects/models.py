from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    HARLEQUIN="Harlequin"
    ALTAMIRA='Altamira'
    BECHT='Becht'
    HOLLANDIA="Hollandia"
    FONDS_CHOICES = [
        (HARLEQUIN, 'Harlequin'),
        (ALTAMIRA, 'Altamira'),
        (BECHT, 'Becht'),
        (HOLLANDIA, 'Hollandia'),
    ]
    # meta details
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    title = models.CharField(max_length=150)
    print_number = models.IntegerField(null=True, blank=True)
    author_surname = models.CharField(max_length=100, null=True, blank=True)
    author_first_names = models.CharField(max_length=100, null=True, blank=True)
    series_name = models.CharField(max_length=100, null=True, blank=True)
    fonds = models.CharField(max_length=100, null=True, blank=True, choices=FONDS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    offer_name = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=100)

    # planning details
    manuscript_due = models.DateField(null=True, blank=True)
    translation_due = models.DateField(null=True, blank=True)
    pre_press_due = models.DateField(null=True, blank=True)
    print_ready_manuscript_due = models.DateField(null=True, blank=True)
    cover_and_artwork_due = models.DateField(null=True, blank=True)
    files_due = models.DateField(null=True, blank=True)
    CB_delivery_due = models.DateField(null=True, blank=True)
    publishing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title + '_' + str(self.print_number)
    
    class Meta:
        ordering = ['-date_created'] # Sorts all returned data by date_created

class PaperbackProject(Project):
    
    # production details
    binding = models.CharField(max_length=100, null=True, blank=True)
    format = models.CharField(max_length=100, null=True, blank=True)
    paper_type = models.CharField(max_length=100, null=True, blank=True)
    print_run = models.IntegerField(null=True, blank=True)
    printer = models.CharField(max_length=100, null=True, blank=True)
    cover_material = models.CharField(max_length=100, null=True, blank=True)
    cover_decoration = models.CharField(max_length=100, null=True, blank=True)
    print = models.CharField(max_length=100, null=True, blank=True)
    dust_jacket = models.CharField(max_length=100, null=True, blank=True)
    extras = models.TextField(null=True, blank=True)

class HardbackProject(Project):
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


class BoxedProject(Project):
    # production details
    box_dimensions = models.CharField(max_length=100, null=True, blank=True)
    box_wrapping_paper = models.CharField(max_length=100, null=True, blank=True)
    box_wrapping_paper_print = models.CharField(max_length=100, null=True, blank=True)
    box_wrapping_finishing = models.CharField(max_length=100, null=True, blank=True)
    box_lining_paper = models.CharField(max_length=100, null=True, blank=True)
    box_lining_paper_print = models.CharField(max_length=100, null=True, blank=True)
    box_hinge = models.CharField(max_length=100, null=True, blank=True)
    box_thumbholes  = models.CharField(max_length=100, null=True, blank=True)
    box_extras = models.TextField(null=True, blank=True)

    cards_format = models.CharField(max_length=100, null=True, blank=True)
    cards_paper_type = models.CharField(max_length=100, null=True, blank=True)
    cards_print = models.CharField(max_length=100, null=True, blank=True)
    cards_rounded_corners = models.CharField(max_length=100, null=True, blank=True)
    cards_finishing = models.CharField(max_length=100, null=True, blank=True)

    book_format = models.CharField(max_length=100, null=True, blank=True)
    book_binding = models.CharField(max_length=100, null=True, blank=True)
    book_paper_type = models.CharField(max_length=100, null=True, blank=True)
    book_print = models.IntegerField(null=True, blank=True)
    book_cover_material = models.CharField(max_length=100, null=True, blank=True)
    book_cover_print = models.CharField(max_length=100, null=True, blank=True)
    book_cover_finishing = models.CharField(max_length=100, null=True, blank=True)
    book_extras = models.TextField(null=True, blank=True)

    print_run = models.IntegerField(null=True, blank=True)
    printer = models.CharField(max_length=100, null=True, blank=True)
    extras = models.TextField(null=True, blank=True)


class Task(models.Model):
    TODO="TO DO"
    COMPLETED='COMPLETED'
    INPROGRESS='IN-PROGRESS'
    STATUS_CHOICES = [
        (TODO, 'TO DO'),
        (INPROGRESS, 'IN-PROGRESS'),
        (COMPLETED, 'COMPLETED'),

    ]
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(null=True,blank=True, verbose_name="Description")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Project")
    assignee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="Assignee")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    due_date = models.DateField(blank=True, verbose_name="Due Date")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= TODO, verbose_name="Status")
    

    def __str__(self):
        return self.title