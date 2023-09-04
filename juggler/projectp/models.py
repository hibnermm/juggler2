from django.contrib import auth
from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=50, help_text="name of project")
  date_created = models.DateTimeField(null=True, help_text="date and time project created")
  def __str__(self):
    return self.name

class Task(models.Model):
  description = models.CharField(max_length=100, help_text="description of task")
  status = models.BooleanField(default=False)
  project = models.ForeignKey(Project,on_delete=models.CASCADE)
  def __str__(self):
    return self.description


"""
Idea - project management 
Possibl models given rationale:
many people might work on many projects
many people might complete many tasks

Models to be worked on...:
class Contact(models.Model):
  first_name = models.CharField(max_length=50, help_text = "contact first name")
  last_name = models.CharField(max_length=50, help_text = "contact last name")
  email = models.EmailField(help_text = "email for contact")
  

class ProjectContacts(models.Model):
  class ContactRoles(models.TextChoices):
    LEAD = "LEAD", "Lead"
    MEMBER = "MEMBER", "Member"
    ANALYST = "ANALYST", "Analyst"
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  role=models.CharField(choices=ContacrtRoles.choices)
"""
   