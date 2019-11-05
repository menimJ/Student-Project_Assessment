from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .manager import CustomUserManager

enum = (
    ('S', 'Student'), ('E', 'Examiner'), ('A', 'Admin'),
)


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=30,
                                help_text="the login username, it is also the matric number of the "
                                          "student")
    role = models.CharField(max_length=30, choices=enum)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    grade = models.FloatField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    project = models.ForeignKey('Project.Project', null=True, blank=True, related_name='assign',
                                on_delete=models.SET_NULL)

    objects = CustomUserManager()

    # @is_admin.setter
    # def foo(self, value):
    #     self.is_admin = value

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Grade(models.Model):
    abstract = models.FloatField(help_text="States the grading value for the section")
    literature = models.FloatField(help_text="States the grading value for the section")
    method = models.FloatField(help_text="States the grading value for the section")
    analysis = models.FloatField(help_text="States the grading value for the section")
    conclusion = models.FloatField(help_text="States the grading value for the section")

# Create your models here.
