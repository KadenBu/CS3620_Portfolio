from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Hobby, Project

# Create your views here.
def home(request):
    return HttpResponse("Hi I'm Kaden, welcome to my portfolio! I like to program and play basketball. Recently I've gotten into snowboarding.")

def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

def portfolio(request):
    project_list = Project.objects.all()
    return HttpResponse(project_list)

def contact(request):
    return HttpResponse("kadenbuchanan@mail.weber.edu")