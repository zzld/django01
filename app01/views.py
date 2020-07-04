from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Students, Grades

def students(request):
    stu = Students.objects.all()
    return render(request,'app01/students.html',{'students':stu})

def grades(request):
    grades = Grades.objects.all()
    return render(request,'app01/grades.html',{'grades':grades})


def login(request):
    return render(request,'app01/login.html')

def main(request):
    return render(request,'app01/main.html')