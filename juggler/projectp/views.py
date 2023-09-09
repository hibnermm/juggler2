from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, "projectp/homepage.html")

def contact(request):
    return render(request, "projectp/contact.html")

def projects(request):
    return render(request, "projectp/projects.html")
    