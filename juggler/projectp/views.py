from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, "projectp/homepage.html")

def contact(request):
    return render(request, "projectp/contact.html")

def projects(request):
    projects = Project.objects.all() 
    projects_list = [ ]
    for project in projects:
        task = project.task_set.all()  
        projects_list.append({'project': project, 'task': task})

    context= {'projects_list': projects_list}
    return render(request, "projectp/projects.html", context)
    


#similar to book_list, in views, "for book in books", book_list.append({'book': book,...})
#in book_list.html, "item.book.title" is this where book defined?

#sql statements modelName.objects.all() retrieve object set
""" {% if item.task.exclude(task = False) %} if
item.task.filter(status__contains=0) {% endif %} {% if item.task.status !=
True%} {% endif %} """