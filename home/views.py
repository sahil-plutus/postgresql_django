from django.shortcuts import render, HttpResponse
from .models import Student


def home(request):
    students = Student.objects.all()
    return HttpResponse(students)