from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from ranking.models import Teacher, Subject, Course
from rest_framework import viewsets
from ranking.serializers import TeacherSerializer

def index(request):
    teachers = Teacher.objects.order_by('-score')[:5]
    return render(request, 'ranking/index.html', {'teachers': teachers})

class TeacherList(ListView):
    model = Teacher

class TeacherDetail(DetailView):
    model = Teacher

class TeacherViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Teachers to be viewd or edited
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer