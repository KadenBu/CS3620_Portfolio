from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Hobby, Project

# Create your views here.
def home(request):
    return HttpResponse("Hi I'm Kaden, welcome to my portfolio! I like to program and play basketball. Recently I've gotten into snowboarding.")

def hobbies(request):
    hobby_list = Hobby.objects.all().values()
    output = ""
    for i in hobby_list:
        output = output + i['name'] + ": "
        output = output + i['desc'] + "<br>"
        output = output + "<br>"
    return HttpResponse(output)

def portfolio(request):
    project_list = Project.objects.all().values()
    output = ""
    for i in project_list:
        output = output + i['name'] + ": "
        output = output + i['desc'] + "<br>"
        output = output + "<br>"
    return HttpResponse(output)

def contact(request):
    return HttpResponse("kadenbuchanan@mail.weber.edu")