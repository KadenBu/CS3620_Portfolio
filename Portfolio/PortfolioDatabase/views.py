from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Hobby, Project
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'PortfolioDatabase/index.html')

def hobbies(request):
    hobby_list = Hobby.objects.all().values()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)

def portfolio(request):
    project_list = Project.objects.all().values()
    context = {
        'project_list': project_list,
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)

def contact(request):
    return render(request, 'PortfolioDatabase/contact.html')

def hobby_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby,
    }
    return render(request, 'PortfolioDatabase/hobby_details.html', context)

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {
        'project': project,
    }
    return render(request, 'PortfolioDatabase/project_details.html', context)