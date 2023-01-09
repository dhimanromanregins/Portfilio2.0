from django.shortcuts import render
from .models import Project_Details

# Create your views here.


def index(request):
    projects = Project_Details.objects.all()
    counter = 0
    for i in projects:
        counter += 1
        print(i,counter, '--------------------------->')
    context = {'projects':projects, 'counter':counter}
    return render(request, 'index.html', context)


def project_detail(request):
    return render(request, 'project_detail.html')