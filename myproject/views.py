from django.shortcuts import render
from django.http import HttpResponse
from .models import MyProject 

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def my_project(request):
    data = MyProject.objects.all()
    return render(request,'my_project.html', {'projects': data})