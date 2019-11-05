from django.db import models
from django.conf import settings


class Project(models.Model):
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='st_project')
    title = models.CharField(max_length=50)
    abstract = models.TextField(help_text=" Student Project Abstract")
    literature = models.TextField(help_text="Student Project Literature")
    method = models.TextField(help_text="Student Project Method")
    analysis = models.TextField(help_text="Student Project Analysis")
    conclusion = models.TextField(help_text=
                                  "Student Project Conclusion")

    class Meta:
        permissions = (
            ('can_view_project', 'Can View Project'),
            ('can_grade_project', 'Can grade Project '),
        )

    def __str__(self):
        return self.title


class Project_files(models.Model):
    title = models.CharField(max_length=50, help_text="The Title of the Project")
    abstract = models.FileField()
    literature = models.FileField()
    method = models.FileField()
    analysis = models.FileField()
    conclusion = models.FileField()

# Create your models here.
